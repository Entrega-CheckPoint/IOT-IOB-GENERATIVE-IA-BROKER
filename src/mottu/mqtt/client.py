# mottu/mqtt/client.py
from datetime import datetime
import hashlib
from random import randint
import paho.mqtt.client as mqtt
import json
from mottu.database.connection import SessionLocal
from mottu.database.models import SensorData
import sqlalchemy



def gerar_hash(id_dispositivo, id_patio, data_hora_registro):
    texto = f"{id_dispositivo}-{id_patio}-{data_hora_registro}"
    return hashlib.sha256(texto.encode()).hexdigest()


def on_connect(client, userdata, flags, rc):
    print("✅ Conectado ao broker com código", rc)
    client.subscribe("sensors/#")


def on_message(client, userdata, msg):
    print(f"📨 Mensagem recebida em {msg.topic}: {msg.payload}")
    try:
        payload = json.loads(msg.payload)
        id_dispositivo = payload.get("Sensor")
        ip_wifi = payload.get("IP")
        intensidade_sinal = payload.get("RSSI")

        """Lógica para triangular a localização da moto
        --> Por enquanto usar valores randomicos
        """
        vl_coordx = randint(0, 100)
        vl_coordy = randint(0, 100)

        # Usar o ip do wifi para encontrar qual é o patio que está localizado
        # id_patio = ip_wifi
        id_patio = 2

        # Data do registro
        dt_registro = datetime.now()

        # Id de registro
        if not id_dispositivo or not ip_wifi:
            print("❌ Payload incompleto!")
            return

        id_posicao = gerar_hash(id_dispositivo, id_patio, dt_registro)

        db = SessionLocal()
        dado = SensorData(
            id_posicao=id_posicao,
            id_dispositivo=id_dispositivo,
            id_patio=id_patio,
            vl_coordx=vl_coordx,
            vl_coordy=vl_coordy,
            dt_registro=dt_registro,
            ds_setor="A2",
        )
        db.add(dado)
        db.commit()
        db.close()

        print("✅ Dado salvo no banco com sucesso!")
    except sqlalchemy.exc.SQLAlchemyError as e:
        print("❌ Erro de banco de dados:", e)

    except Exception as e:
        print("❌ Erro ao processar mensagem:", e)


print("🚀 Iniciando cliente MQTT...")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("py-mosquitto", 1883)
# client.connect("localhost", 1883)
client.loop_forever()
