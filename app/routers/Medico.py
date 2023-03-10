from typing import List
from fastapi import APIRouter, Response, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schemas.MedicoSchema import MedicoSchema
from models.MedicoModels import MedicoModels


router = APIRouter()
from core.deps import get_session
#post Medico
@router.post("/medico", response_model=MedicoSchema, status_code=status.HTTP_201_CREATED)
async def post_medico(medico: MedicoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MedicoModels).filter(MedicoModels.nome == medico.nome)
        result = await session.execute(query)
        medico = result.scalars().unique().one_or_none()

        if medico:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Médico já cadastrado")

        medico = MedicoModels(nome=medico.nome, crm=medico.crm, cpf=medico.cpf, rg=medico.rg, data_nascimento=medico.data_nascimento, sexo=medico.sexo, telefone=medico.telefone, email=medico.email, endereco=medico.endereco, numero=medico.numero, complemento=medico.complemento, bairro=medico.bairro, cidade=medico.cidade, estado=medico.estado, cep=medico.cep, especialidade=medico.especialidade)
        session.add(medico)
        await session.commit()
        await session.refresh(medico)
        return medico
    
#put Medico
@router.put("/medico/{id}", response_model=MedicoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_medico(id: int, medico: MedicoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MedicoModels).filter(MedicoModels.id == id)
        result = await session.execute(query)
        medico = result.scalars().unique().one_or_none()

        if medico is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Médico não encontrado")

        medico.nome = medico.nome
        medico.crm = medico.crm
        medico.cpf = medico.cpf
        medico.rg = medico.rg
        medico.data_nascimento = medico.data_nascimento
        medico.sexo = medico.sexo
        medico.telefone = medico.telefone
        medico.email = medico.email
        medico.endereco = medico.endereco
        medico.numero = medico.numero
        medico.complemento = medico.complemento
        medico.bairro = medico.bairro
        medico.cidade = medico.cidade
        medico.estado = medico.estado
        medico.cep = medico.cep
        medico.especialidade = medico.especialidade
        await session.commit()
        await session.refresh(medico)
        return medico
    
#delete Medico
@router.delete("/medico/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_medico(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MedicoModels).filter(MedicoModels.id == id)
        result = await session.execute(query)
        medico = result.scalars().unique().one_or_none()

        if medico is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Médico não encontrado")

        session.delete(medico)
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
#get Medico
@router.get("/medico/{id}", response_model=MedicoSchema, status_code=status.HTTP_200_OK)
async def get_medico(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MedicoModels).filter(MedicoModels.id == id)
        result = await session.execute(query)
        medico = result.scalars().unique().one_or_none()

        if medico is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Médico não encontrado")

        return medico
    
    
#get all Medico
@router.get("/medico", response_model=List[MedicoSchema], status_code=status.HTTP_200_OK)
async def get_all_medico(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MedicoModels)
        result = await session.execute(query)
        medico = result.scalars().all()

        if medico is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Médico não encontrado")

        return medico

