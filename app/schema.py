from pydantic import BaseModel
from typing import Optional

class ExtractRequest(BaseModel):
    text: str

class ExtractResponse(BaseModel):
    valor_ir: Optional[float] = None
    aliquota_ir: Optional[float] = None
    base_calculo_ir: Optional[float] = None
    valor_iof: Optional[float] = None
    aliquota_iof: Optional[float] = None
    valor_pis: Optional[float] = None
    valor_cofins: Optional[float] = None
    valor_cide: Optional[float] = None 