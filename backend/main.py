from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Ilha da Sorte")

# Caminho absoluto do frontend
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# Servir arquivos estáticos (HTML, CSS, JS)
app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")

# Página inicial
@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "inicio.html")

# Rotas de páginas
@app.get("/rifa")
def rifa():
    return FileResponse(FRONTEND_DIR / "rifa_detail.html")

@app.get("/checkout")
def checkout():
    return FileResponse(FRONTEND_DIR / "checkout.html")

@app.get("/meus-bilhetes")
def meus_bilhetes():
    return FileResponse(FRONTEND_DIR / "meus_bilhetes.html")

@app.get("/dashboard")
def dashboard():
    return FileResponse(FRONTEND_DIR / "dashboard.html")

# 👉 IMPORTANTE:
# Aqui você continua importando suas rotas de API
# app.include_router(rifas_router)
# app.include_router(pedidos_router)
# app.include_router(admin_router)
