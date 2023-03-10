from pydantic import BaseSettings

from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    
    DB_URL :str = "postgresql+asyncpg://postgres:admin@localhost:5432/prontuario"
    DB_BASE_MODEL = declarative_base()

    JWT_SECRET = "OTJs0qDq45OGL6rhlrOwmQWhhGgrHTUzOg"

    """
    import secrets 

    token = secrets.token_urlsafe(25)

    print(token)
    """

    ALGHORITM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()


