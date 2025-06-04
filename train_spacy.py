import spacy
from spacy.training import Example
from spacy.util import minibatch
import pandas as pd
import random
import os

TRAIN_DATA_PATH = 'data/treino_spacy.csv'
VALID_DATA_PATH = 'data/validacao_spacy.csv'
MODEL_DIR = 'model'

# Função para converter CSV para formato spaCy NER
# Espera-se que o CSV tenha colunas: 'text', 'entities' (entities como lista de tuplas: [(start, end, label), ...])
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    data = []
    for _, row in df.iterrows():
        ents = eval(row['entities']) if isinstance(row['entities'], str) else row['entities']
        data.append((row['text'], {'entities': ents}))
    return data

train_data = load_data(TRAIN_DATA_PATH)
valid_data = load_data(VALID_DATA_PATH)

nlp = spacy.blank('pt')
if 'ner' not in nlp.pipe_names:
    ner = nlp.add_pipe('ner')
else:
    ner = nlp.get_pipe('ner')

# Adiciona labels
for _, annots in train_data:
    for ent in annots['entities']:
        ner.add_label(ent[2])

# Treinamento
optimizer = nlp.begin_training()
for itn in range(20):
    random.shuffle(train_data)
    losses = {}
    batches = minibatch(train_data, size=8)
    for batch in batches:
        examples = [Example.from_dict(nlp.make_doc(text), annots) for text, annots in batch]
        nlp.update(examples, drop=0.3, losses=losses)
    print(f"Iter {itn+1}, Loss: {losses['ner']:.2f}")

# Salva modelo
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
nlp.to_disk(MODEL_DIR)
print(f"Modelo salvo em {MODEL_DIR}")

# Validação
correct = 0
pred_total = 0
true_total = 0
for text, annots in valid_data:
    doc = nlp(text)
    pred_ents = set((ent.start_char, ent.end_char, ent.label_) for ent in doc.ents)
    true_ents = set((ent[0], ent[1], ent[2]) for ent in annots['entities'])
    correct += len(pred_ents & true_ents)
    pred_total += len(pred_ents)
    true_total += len(true_ents)

precision = correct / pred_total if pred_total else 0
recall = correct / true_total if true_total else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0
print(f"Precisão: {precision:.2%}, Recall: {recall:.2%}, F1: {f1:.2%}") 