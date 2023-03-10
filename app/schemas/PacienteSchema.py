from pydantic import BaseModel
from typing import Optional

class PacienteSchema(BaseModel):
    id: Optional[int]
    nome: str
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
    nome_mae: str
    nome_pai: str
    profissao: str
    estado_civil: str
    convenio: str
    numero_convenio: str
    nome_convenio: str
    tipo_sanguineo: str
    fator_rh: str
    peso: str
    altura: str
    imc: str
    class Config:
        orm_mode = True
