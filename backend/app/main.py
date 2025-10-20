from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="Monitoramento da Poluição do Ar")

# Registrar rotas
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "API de Monitoramento da Poluição do Ar está funcionando!"}