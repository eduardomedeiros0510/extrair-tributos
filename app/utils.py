import spacy
import os

# Carrega o modelo spaCy customizado
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "spacy_model")
nlp = spacy.load(MODEL_PATH)

def extract_tax_info(text):
    doc = nlp(text)
    # Inicializa o dicionário de resposta
    response = {
        "VALOR_IOF": None,
        "VALOR_IR": None,
        "VALOR_PIS": None,
        "VALOR_COFINS": None,
        "VALOR_CIDE": None,
        "ALIQUOTA_IOF": None,
        "ALIQUOTA_IR": None,
        "BASE_CALCULO_IR": None
    }
    # Extrai entidades do texto
    for ent in doc.ents:
        label = ent.label_.upper()
        value = ent.text
        if label == "VALOR_IOF":
            response["VALOR_IOF"] = value
        elif label == "VALOR_IR":
            response["VALOR_IR"] = value
        elif label == "VALOR_PIS":
            response["VALOR_PIS"] = value
        elif label == "VALOR_COFINS":
            response["VALOR_COFINS"] = value
        elif label == "VALOR_CIDE":
            response["VALOR_CIDE"] = value
        elif label == "ALIQUOTA_IOF":
            response["ALIQUOTA_IOF"] = value
        elif label == "ALIQUOTA_IR":
            response["ALIQUOTA_IR"] = value
        elif label == "BASE_CALCULO_IR":
            response["BASE_CALCULO_IR"] = value
    return response 