from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class MedicoModels(settings.DB_BASE_MODEL):
    __tablename__ = "medico"

    id_medico = Column(Integer, primary_key=True, index=True)
    crm = Column(String)
    especialidade = Column(String)
    id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("UsuarioModel", back_populates="medico")
    paciente = relationship("PacienteModels", back_populates="medico", uselist=True,
                            cascade="all, delete, delete-orphan")