# src/mottu/database/connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Dados do banco
DB_USER = "pyser"
DB_PASSWORD = "pypass"
# DB_HOST = "localhost"
DB_HOST = "py-mysql"
DB_PORT = "3306"
DB_NAME = "pyDB"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criação da engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Session para uso com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os models
Base = declarative_base()
