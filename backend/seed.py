"""
Arquivo para popular o banco com dados iniciais de teste
Execute apenas uma vez
"""

from database import SessionLocal
from models.rifa import Rifa
from models.numero import Numero

db = SessionLocal()

# Evita duplicar seed
if db.query(Rifa).count() == 0:
    rifa = Rifa(
        nome="iPhone 15 Pro Max",
        descricao="Concorra a um iPhone 15 Pro Max lacrado",
        preco=10.0,
        total_numeros=100
    )

    db.add(rifa)
    db.commit()
    db.refresh(rifa)

    # Cria os números da rifa (01 a 100)
    for i in range(1, rifa.total_numeros + 1):
        numero = Numero(
            rifa_id=rifa.id,
            numero=str(i).zfill(2)
        )
        db.add(numero)

    db.commit()
    print("Seed criada com sucesso 🚀")
else:
    print("Seed já existe.")
