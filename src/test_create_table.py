# src/mottu/database/test_create_tables.py

from mottu.database.connection import Base, engine
import mottu.database.models  # Importa os models pra registrar as classes

Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")
