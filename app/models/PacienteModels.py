from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class PacienteModels(settings.DB_BASE_MODEL):

    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String)
    rg = Column(String)
    data_nascimento = Column(String)
    sexo = Column(String)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    numero = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String)
    nome_mae = Column(String)
    nome_pai = Column(String)
    profissao = Column(String)
    estado_civil = Column(String)
    convenio = Column(String)
    numero_convenio = Column(String)
    nome_convenio = Column(String)
    tipo_sanguineo = Column(String)
    fator_rh = Column(String)
    peso = Column(String)
    altura = Column(String)
    imc = Column(String)

    # Relacionamentos
    # paciente_id = Column(Integer, ForeignKey("paciente.id"))
    # paciente = relationship("PacienteModels", back_populates="paciente")

    def __repr__(self):
        return f"PacienteModels(nome={self.nome!r})"
