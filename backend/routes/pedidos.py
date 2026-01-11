from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.pedido import Pedido
from models.numero import Numero
from services.pagamentos import criar_pagamento_pix


router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/")
def criar_pedido(dados: dict, db: Session = Depends(get_db)):
    """
    Cria pedido e reserva números
    """
    numeros = dados["numeros"].split(",")

    # Verifica se números estão livres
    for n in numeros:
        num = db.query(Numero).filter(
            Numero.rifa_id == dados["rifa_id"],
            Numero.numero == n,
            Numero.status == "livre"
        ).first()
        if not num:
            raise HTTPException(status_code=400, detail=f"Número {n} indisponível")

    # Reserva números
    for n in numeros:
        num = db.query(Numero).filter(
            Numero.rifa_id == dados["rifa_id"],
            Numero.numero == n
        ).first()
        num.status = "reservado"

    pedido = Pedido(**dados)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    return pedido

@router.get("/meus-bilhetes")
def meus_bilhetes(cpf: str, db: Session = Depends(get_db)):
    """
    Retorna pedidos por CPF (simples e sem login)
    """
    pedidos = db.query(Pedido).filter(Pedido.cpf == cpf).all()
    return pedidos

@router.post("/{pedido_id}/pix")
def gerar_pix(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    pagamento = criar_pagamento_pix(pedido.id, pedido.valor_total)
    return pagamento
