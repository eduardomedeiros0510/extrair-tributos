from pydantic import BaseModel
from typing import Optional

class TributoInfo(BaseModel):
    valor: Optional[float]
    aliquota: Optional[float]
    base_calculo: Optional[float]

class ExtracaoResponse(BaseModel):
    valor_iof: Optional[float]
    valor_ir: Optional[float]
    valor_pis: Optional[float]
    valor_cofins: Optional[float]
    valor_cide: Optional[float]
    aliquota_iof: Optional[float]
    aliquota_ir: Optional[float]
    base_calculo_ir: Optional[float] 