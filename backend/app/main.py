from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router

app = FastAPI(title="Monitoramento da Poluição do Ar")

# Configuração do CORS
origins = [
    "http://localhost:5173",
    "http://172.22.115.174",
    "https://062cbe10025c.ngrok-free.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "API de Monitoramento da Poluição do Ar está funcionando!"}
