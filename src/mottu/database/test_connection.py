# src/mottu/database/test_connection.py
from sqlalchemy import text
from connection import SessionLocal

try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))
    print("✅ Conexão bem-sucedida!")
except Exception as e:
    print("❌ Erro ao conectar:", e)
finally:
    db.close()
