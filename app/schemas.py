from pydantic import BaseModel
from typing import Optional

class ExtractRequest(BaseModel):
    text: str

class ExtractResponse(BaseModel):
    VALOR_IOF: Optional[str]
    VALOR_IR: Optional[str]
    VALOR_PIS: Optional[str]
    VALOR_COFINS: Optional[str]
    VALOR_CIDE: Optional[str]
    ALIQUOTA_IOF: Optional[str]
    ALIQUOTA_IR: Optional[str]
    BASE_CALCULO_IR: Optional[str] 