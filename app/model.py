import spacy
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model')

class TributaryExtractor:
    def __init__(self):
        self.nlp = spacy.load(MODEL_PATH)

    def extract(self, text: str):
        doc = self.nlp(text)
        result = {
            'valor_ir': None,
            'aliquota_ir': None,
            'base_calculo_ir': None,
            'valor_iof': None,
            'aliquota_iof': None,
            'valor_pis': None,
            'valor_cofins': None,
            'valor_cide': None
        }
        for ent in doc.ents:
            label = ent.label_.lower()
            value = ent.text.replace('%', '').replace('R$', '').replace(',', '.').strip()
            try:
                value = float(value)
            except Exception:
                continue
            if label == 'valor_ir':
                result['valor_ir'] = value
            elif label == 'aliquota_ir':
                result['aliquota_ir'] = value
            elif label == 'base_calculo_ir':
                result['base_calculo_ir'] = value
            elif label == 'valor_iof':
                result['valor_iof'] = value
            elif label == 'aliquota_iof':
                result['aliquota_iof'] = value
            elif label == 'valor_pis':
                result['valor_pis'] = value
            elif label == 'valor_cofins':
                result['valor_cofins'] = value
            elif label == 'valor_cide':
                result['valor_cide'] = value
        return result 