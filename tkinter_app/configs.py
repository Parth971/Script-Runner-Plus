import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

MQTT_BROKER_HOST = os.getenv('MQTT_BROKER_HOST')
MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT'))
MQTT_TOPIC_SCRIPT_UPDATES = "topic/script_updates"

db = PostgresqlDatabase(
    database=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT'),
)