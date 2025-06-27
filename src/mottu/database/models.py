# src/mottu/database/models.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from mottu.database.connection import Base

class SensorData(Base):
    __tablename__ = "T_CM_POSICAO_MOTO"

    id_posicao = Column(String(64),name= 'ID_POSICAO', primary_key=True)
    id_dispositivo = Column(Integer, name="ID_DISPOSITIVO", nullable=False)
    id_patio = Column(Integer, name="ID_PATIO", nullable=False)
    vl_coordx = Column(Float, name="VL_COORDX", nullable=False)
    vl_coordy = Column(Float, name="VL_COORDY", nullable=False)
    dt_registro = Column(DateTime, name="DT_REGISTRO", nullable=False, default=datetime.now())
    ds_setor = Column(String(50), name="DS_SETOR", nullable=True)
