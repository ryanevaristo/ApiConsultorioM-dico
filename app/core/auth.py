from pytz import timezone
from typing import Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer


from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from models.UsuarioModel import UsuarioModel
from core.configs import settings
from core.security import verificar_senha

from pydantic import EmailStr



oauth2_schema = OAuth2PasswordBearer (
    tokenUrl=f"/usuario/login" # mesma url de login
)


async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        print(usuario)
        if not usuario:
            print("Usuario não encontrado")
            return None
        

        if not verificar_senha(senha, usuario.senha):
            print("Usuario não encontrado")
            return None

        return usuario



def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    payload = {}
    sp = timezone('America/Sao_Paulo')
    tempo_expira = datetime.now(tz=sp) + tempo_vida

    payload["type"] = tipo_token
    payload["exp"] = tempo_expira
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)

    return jwt.encode(payload,settings.JWT_SECRET,algorithm=settings.ALGHORITM)



def criar_acesso_token(sub: str) -> str:
    """
    visitar o site : jwt.io
    """
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )