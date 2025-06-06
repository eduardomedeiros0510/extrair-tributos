import spacy
from spacy.tokens import DocBin
import pandas as pd
import os
from sklearn.metrics import precision_score, recall_score, f1_score

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data')
TRAIN_FILE = os.path.join(DATA_DIR, 'treino_spacy.csv')
VAL_FILE = os.path.join(DATA_DIR, 'validacao_spacy.csv')
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'nlp_model')

LABELS = [
    'VALOR_IOF', 'VALOR_IR', 'VALOR_PIS', 'VALOR_COFINS', 'VALOR_CIDE',
    'ALIQUOTA_IOF', 'ALIQUOTA_IR', 'BASE_CALCULO_IR'
]

# Função para converter CSV para formato spaCy
def convert_csv_to_spacy(csv_file, output_path):
    nlp = spacy.blank('pt')
    db = DocBin()
    df = pd.read_csv(csv_file, header=None)
    for _, row in df.iterrows():
        text = row[0]
        ents_str = str(row[1]).strip()
        if not ents_str or ents_str.lower() in ["nan", "none", ""]:
            ents = []
        else:
            if ents_str.startswith("entities"):
                parts = ents_str.split("=", 1)
                if len(parts) > 1:
                    ents_str = parts[1].strip()
                else:
                    ents_str = ""
            try:
                ents = eval(ents_str) if ents_str else []
            except Exception:
                ents = []
        doc = nlp.make_doc(text)
        ents_spacy = []
        for start, end, label in ents:
            if label in LABELS:
                ents_spacy.append(doc.char_span(start, end, label=label))
        doc.ents = [e for e in ents_spacy if e is not None]
        db.add(doc)
    db.to_disk(output_path)

# Preparar dados
os.makedirs('app/model/tmp', exist_ok=True)
convert_csv_to_spacy(TRAIN_FILE, 'app/model/tmp/train.spacy')
convert_csv_to_spacy(VAL_FILE, 'app/model/tmp/val.spacy')

# Treinamento
nlp = spacy.blank('pt')
if 'ner' not in nlp.pipe_names:
    ner = nlp.add_pipe('ner')
else:
    ner = nlp.get_pipe('ner')
for label in LABELS:
    ner.add_label(label)

train_data = list(DocBin().from_disk('app/model/tmp/train.spacy').get_docs(nlp.vocab))
val_data = list(DocBin().from_disk('app/model/tmp/val.spacy').get_docs(nlp.vocab))

import random
from spacy.training.example import Example

optimizer = nlp.begin_training()
for itn in range(20):
    random.shuffle(train_data)
    losses = {}
    batches = spacy.util.minibatch(train_data, size=4)
    for batch in batches:
        examples = [Example.from_dict(doc, {"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]}) for doc in batch]
        nlp.update(examples, drop=0.3, losses=losses)
    print(f"Iteration {itn+1}, Losses: {losses}")

# Salvar modelo
os.makedirs(MODEL_DIR, exist_ok=True)
nlp.to_disk(MODEL_DIR)

# Validação
true_labels = []
pred_labels = []
for doc in val_data:
    pred = nlp(doc.text)
    gold_ents = {(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents}
    pred_ents = {(ent.start_char, ent.end_char, ent.label_) for ent in pred.ents}
    for label in LABELS:
        true_labels.append(int(any(e[2] == label for e in gold_ents)))
        pred_labels.append(int(any(e[2] == label for e in pred_ents)))

precision = precision_score(true_labels, pred_labels)
recall = recall_score(true_labels, pred_labels)
f1 = f1_score(true_labels, pred_labels)

print(f"Validação - Precision: {precision:.2f}, Recall: {recall:.2f}, F1: {f1:.2f}") 