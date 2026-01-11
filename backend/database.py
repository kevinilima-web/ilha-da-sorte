from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import DATABASE_URL

# Cria conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)

# Sessão do banco (usada nas rotas)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos os models
Base = declarative_base()

# Função para injetar sessão nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
