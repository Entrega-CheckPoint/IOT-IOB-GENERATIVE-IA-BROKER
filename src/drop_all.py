from mottu.database.connection import Base, engine
from mottu.database import models  # Garante que os modelos sejam "vistos"


print("💥 Apagando todas as tabelas...")
Base.metadata.drop_all(bind=engine)
print("✅ Tabelas removidas com sucesso.")
