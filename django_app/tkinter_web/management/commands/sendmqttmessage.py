import logging

from django.conf import settings
from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt

logger = logging.getLogger(__file__)


class Command(BaseCommand):
    help = 'Sends a messages to the MQTT client'
    MQTT_TOPIC_SCRIPT_UPDATES = "topic/script_updates"

    def handle(self, *args, **options):
        mqtt_client = mqtt.Client()
        logger.info(f'MQTT_SERVER : {settings.MQTT_SERVER} | MQTT_PORT : {settings.MQTT_PORT}')
        mqtt_client.connect(settings.MQTT_SERVER, settings.MQTT_PORT)
        message = f"Test message........"
        mqtt_client.publish(self.MQTT_TOPIC_SCRIPT_UPDATES, message)
        logger.info('Test message sent to MQTT')
        mqtt_client.disconnect()
