from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

class UsuarioModel(settings.DB_BASE_MODEL):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    cpf = Column(String)
    rg = Column(String)
    data_nascimento = Column(Date)
    sexo = Column(String)
    telefone = Column(String)
    senha = Column(String)

    medico = relationship("MedicoModels", back_populates="usuario", cascade="all, delete, delete-orphan")
    paciente = relationship("PacienteModels", back_populates="usuario", cascade="all, delete, delete-orphan")
