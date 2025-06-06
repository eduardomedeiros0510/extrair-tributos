import spacy
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'nlp_model')

ENT_MAP = {
    'VALOR_IOF': 'VALOR_IOF',
    'VALOR_IR': 'VALOR_IR',
    'VALOR_PIS': 'VALOR_PIS',
    'VALOR_COFINS': 'VALOR_COFINS',
    'VALOR_CIDE': 'VALOR_CIDE',
    'ALIQUOTA_IOF': 'ALIQUOTA_IOF',
    'ALIQUOTA_IR': 'ALIQUOTA_IR',
    'BASE_CALCULO_IR': 'BASE_CALCULO_IR',
}

def load_model():
    return spacy.load(MODEL_PATH)

def extract_tributos(text, nlp=None):
    if nlp is None:
        nlp = load_model()
    doc = nlp(text)
    result = {k: None for k in ENT_MAP.values()}
    for ent in doc.ents:
        if ent.label_ in ENT_MAP:
            # Pega apenas o valor numérico
            value = ent.text
            value = value.replace('R$', '').replace('%', '').replace(':', '').replace('|', '').strip()
            value = value.replace(',', '.')
            result[ENT_MAP[ent.label_]] = value
    return result 