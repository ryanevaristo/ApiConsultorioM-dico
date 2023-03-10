from typing import List
from fastapi import APIRouter, Response, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas.PacienteSchema import PacienteSchema
from models.PacienteModels import PacienteModels

from core.deps import get_session

router = APIRouter()

# Create a new patient
@router.post("/paciente", response_model=PacienteSchema)
async def post_paciente(paciente: PacienteSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PacienteModels).filter(PacienteModels.nome == paciente.nome)
        result = await session.execute(query)
        paciente = result.scalars().unique().one_or_none()

        if paciente:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Paciente já cadastrado")

        paciente = PacienteModels(nome=paciente.nome, cpf=paciente.cpf, rg=paciente.rg, data_nascimento=paciente.data_nascimento, sexo=paciente.sexo, telefone=paciente.telefone, email=paciente.email, endereco=paciente.endereco, numero=paciente.numero, complemento=paciente.complemento, bairro=paciente.bairro, cidade=paciente.cidade, estado=paciente.estado, cep=paciente.cep)
        session.add(paciente)
        await session.commit()
        await session.refresh(paciente)
        return paciente
    

# Get all patients
@router.get("/paciente", response_model=List[PacienteSchema])
async def get_pacientes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PacienteModels)
        result = await session.execute(query)
        pacientes = result.scalars().all()
        return pacientes
    
# Get a patient by id
@router.get("/paciente/{id}", response_model=PacienteSchema)
async def get_paciente(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PacienteModels).filter(PacienteModels.id == id)
        result = await session.execute(query)
        paciente = result.scalars().unique().one_or_none()

        if paciente is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")

        return paciente
    
# Update a patient by id
@router.put("/paciente/{id}", response_model=PacienteSchema)
async def put_paciente(id: int, paciente: PacienteSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PacienteModels).filter(PacienteModels.id == id)
        result = await session.execute(query)
        paciente = result.scalars().unique().one_or_none()

        if paciente is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")

        paciente.nome = paciente.nome
        paciente.cpf = paciente.cpf
        paciente.rg = paciente.rg
        paciente.data_nascimento = paciente.data_nascimento
        paciente.sexo = paciente.sexo
        paciente.telefone = paciente.telefone
        paciente.email = paciente.email
        paciente.endereco = paciente.endereco
        paciente.numero = paciente.numero
        paciente.complemento = paciente.complemento
        paciente.bairro = paciente.bairro
        paciente.cidade = paciente.cidade
        paciente.estado = paciente.estado
        paciente.cep = paciente.cep
        await session.commit()
        await session.refresh(paciente)
        return paciente
    
# Delete a patient by id
@router.delete("/paciente/{id}")
async def delete_paciente(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PacienteModels).filter(PacienteModels.id == id)
        result = await session.execute(query)
        paciente = result.scalars().unique().one_or_none()

        if paciente is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")

        session.delete(paciente)
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)