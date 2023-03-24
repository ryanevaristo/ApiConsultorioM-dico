from pydantic import BaseModel
from typing import Optional

class MedicoSchema(BaseModel):
    id: Optional[int]
    crm: str
    especialidade: str
    paciente_id: Optional[int]
    class Config:
        orm_mode = True
