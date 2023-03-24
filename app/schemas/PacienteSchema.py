from pydantic import BaseModel
from typing import Optional
from datetime import date

class PacienteSchema(BaseModel):
    id_paciente: Optional[int]
    convenio: str
    numero_convenio: str
    profissao: str
    estado_civil: str
    tipo_sanguineo: str

    class Config:
        orm_mode = True
