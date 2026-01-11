from sqlalchemy import Column, Integer, ForeignKey, String
from database import Base

class Numero(Base):
    """
    Representa um número da rifa
    """
    __tablename__ = "numeros"

    id = Column(Integer, primary_key=True, index=True)
    rifa_id = Column(Integer, ForeignKey("rifas.id"))
    numero = Column(String, nullable=False)

    # status: livre | reservado | vendido
    status = Column(String, default="livre")
