from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class PacienteModels(settings.DB_BASE_MODEL):

    __tablename__ = "paciente"

    id_paciente = Column(Integer, primary_key=True, index=True)
    convenio = Column(String)
    numero_convenio = Column(String)
    profissao = Column(String)
    estado_civil = Column(String)
    tipo_sanguineo = Column(String)

    # Relacionamentos
    id = Column(Integer, ForeignKey("usuario.id"),primary_key=True )
    usuario = relationship("UsuarioModel", back_populates="paciente")
    id_medico = Column(Integer, ForeignKey("medico.id_medico"))
    medico = relationship("MedicoModels", back_populates="paciente")



