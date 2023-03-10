from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class MedicoModels(settings.DB_BASE_MODEL):
    __tablename__ = "medico"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    crm = Column(String)
    cpf = Column(String)
    rg = Column(String)
    data_nascimento = Column(String)
    sexo = Column(String)
    especialidade = Column(String)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    numero = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String)
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    paciente = relationship("PacienteModels", back_populates="medico")

    def __str__(self):
        return f"MedicoModels(id={self.id}, nome={self.nome}, crm={self.crm}, especialidade={self.especialidade}, telefone={self.telefone}, email={self.email}, endereco={self.endereco}, numero={self.numero}, complemento={self.complemento}, bairro={self.bairro}, cidade={self.cidade}, estado={self.estado}, cep={self.cep}, paciente_id={self.paciente_id}, paciente={self.paciente})"