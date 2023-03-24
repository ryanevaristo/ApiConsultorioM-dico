from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioSchemaBase(BaseModel):
    nome: str
    cpf: str
    rg: str
    data_nascimento: date
    sexo: str
    telefone: str
    email: str
    senha: str
    class Config:
        orm_mode = True

class UsuarioSchemaUpdate(UsuarioSchemaBase):
    nome: Optional[str]
    cpf: Optional[str]
    rg: Optional[str]
    data_nascimento: Optional[date]
    sexo: Optional[str]
    telefone: Optional[str]
    email: Optional[str]
    senha: Optional[str]

class UsuarioSchemaCreate(UsuarioSchemaBase):
    Optional[int]
    nome: str
    cpf: str
    rg: str
    data_nascimento: date
    sexo: str
    telefone: str
    email: str
    senha: str