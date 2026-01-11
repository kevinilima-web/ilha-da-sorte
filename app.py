from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
@app.get("/rifas")
def listar_rifas():
    return [
        {
            "id": 1,
            "nome": "iPhone 15",
            "preco": 0.10
        },
        {
            "id": 2,
            "nome": "PS5",
            "preco": 0.25
        }
    ]
