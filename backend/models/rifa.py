from sqlalchemy import Column, Integer, String, Float
from database import Base

class Rifa(Base):
    """
    Representa uma rifa no sistema
    """
    __tablename__ = "rifas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    total_numeros = Column(Integer, nullable=False)

    # status: ativa | encerrada | sorteada
    status = Column(String, default="ativa")
