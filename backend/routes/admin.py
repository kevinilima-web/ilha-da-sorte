from fastapi import APIRouter, Depends, HTTPException, Header

router = APIRouter(prefix="/admin", tags=["Admin"])

ADMIN_TOKEN = "ilhasorte123"

def verificar_admin(token: str = Header(None)):
    if token != ADMIN_TOKEN:
        raise HTTPException(status_code=403, detail="Acesso negado")

@router.get("/dashboard", dependencies=[Depends(verificar_admin)])
def dashboard():
    return {"status": "Admin autorizado"}
