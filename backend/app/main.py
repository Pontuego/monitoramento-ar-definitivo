from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router

app = FastAPI(title="Monitoramento da Poluição do Ar")

# Configuração do CORS
origins = [
    "http://localhost:5173",                   # Se estiver rodando Flutter Web local
    "http://127.0.0.1:5173",
    "https://0c3476319a2d.ngrok-free.app"     # URL gerada pelo ngrok
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