from pydantic import BaseModel
from typing import Optional

class MedicoSchema(BaseModel):
    id: Optional[int]
    nome: str
    crm: str
    cpf: str
    rg: str
    data_nascimento: str
    sexo: str
    telefone: str
    email: str
    endereco: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    estado: str
    cep: str
    especialidade: str
    class Config:
        orm_mode = True