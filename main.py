from fastapi import FastAPI
from cursos import router as cursos_router
from estudantes import router as estudantes_router

app = FastAPI()

# Registrar os roteadores
app.include_router(cursos_router, prefix="/cursos", tags=["Cursos"])
app.include_router(estudantes_router, prefix="/estudantes", tags=["Estudantes"])

@app.get("/")
def root():
    """
    Endpoint raiz da aplicação.
    """
    return {"message": "Bem-vindo à API de Cursos e Estudantes!"}
