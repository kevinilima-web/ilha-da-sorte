from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.rifa import Rifa
from models.numero import Numero

router = APIRouter(prefix="/rifas", tags=["Rifas"])

@router.get("/")
def listar_rifas(db: Session = Depends(get_db)):
    return db.query(Rifa).all()

@router.get("/{rifa_id}")
def detalhe_rifa(rifa_id: int, db: Session = Depends(get_db)):
    rifa = db.query(Rifa).filter(Rifa.id == rifa_id).first()
    if not rifa:
        raise HTTPException(status_code=404, detail="Rifa não encontrada")

    numeros = db.query(Numero).filter(Numero.rifa_id == rifa_id).all()
    vendidos = [n.numero for n in numeros if n.status == "vendido"]

    return {
        "rifa": rifa,
        "numeros": [n.numero for n in numeros],
        "vendidos": vendidos
    }
