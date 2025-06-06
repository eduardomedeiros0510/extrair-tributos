import spacy
from typing import Dict, Any

# Carregue um modelo spaCy (pode ser customizado depois)
nlp = spacy.blank('pt')

# Exemplo de função de extração (mock, para customização futura)
def extrair_tributos(texto: str) -> Dict[str, Any]:
    # Aqui você implementaria a lógica de NER para extrair os tributos
    # Por enquanto, retorna valores mockados para exemplo
    return {
        'valor_iof': 100.0,
        'valor_ir': 200.0,
        'valor_pis': 50.0,
        'valor_cofins': 30.0,
        'valor_cide': 10.0,
        'aliquota_iof': 0.38,
        'aliquota_ir': 0.15,
        'base_calculo_ir': 1333.33
    } 