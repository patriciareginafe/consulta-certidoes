from fastapi import FastAPI

app = FastAPI(
    title="Consulta de Certidões",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "status": "online",
        "sistema": "Consulta Automática de Certidões",
        "versao": "1.0.0"
    }
