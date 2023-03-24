from routers.Medico import router as medico_router
from routers.Paciente import router as paciente_router
from routers.Usuario import router as usuario_router
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()
app = FastAPI(
    title="API - Consultório Médico",
    description="API para o gerenciamento de consultório médico",
    version="1.0.0",
)

@router.get("/")
async def home():
    return {"message": "Bem vindo a API do Consultório Médico"}


app.include_router(router=medico_router, prefix="/medico", tags=["Médico"])
app.include_router(router=paciente_router, prefix="/paciente", tags=["Paciente"])
app.include_router(router=router,  tags=["Home"])
app.include_router(router=usuario_router, prefix="/usuario", tags=["Usuário"])
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0" ,port=8000, reload=True)

