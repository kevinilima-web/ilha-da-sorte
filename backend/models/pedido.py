from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Pedido(Base):
    """
    Pedido realizado por um cliente
    """
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    rifa_id = Column(Integer, ForeignKey("rifas.id"))

    nome_cliente = Column(String, nullable=False)
    whatsapp = Column(String, nullable=False)
    cpf = Column(String, nullable=False)

    numeros = Column(String, nullable=False)  # "01,02,15"
    valor_total = Column(Float, nullable=False)

    # status: pendente | pago | cancelado
    status_pagamento = Column(String, default="pendente")
