import json
from datetime import datetime

import paho.mqtt.client as mqtt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
import logging

from django.core.serializers.json import DjangoJSONEncoder

from tkinter_web.consumers import RealTimeConsumer
from tkinter_web.models import Script, ExecutionLog

logger = logging.getLogger(__file__)


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%b. %d, %Y, %I:%M %p")
        return super().default(obj)

def on_message(mqtt_client, userdata, message):
    try:
        payload = json.loads(message.payload.decode("utf-8"))

        _id = payload.get("id")
        action = payload.get("action")

        if _id and action:
            print(f'Received JSON message on topic: {message.topic} with script_id: {_id} and action: {action}')
            logger.info(
                f'Received JSON message on topic: {message.topic} with script_id: {_id} and action: {action}'
            )

            res = None

            if action in ['create', 'update']:
                script = Script.objects.get(id=_id)
                res = {
                    'action': action,
                    'data': {
                        'script_id': _id,
                        'script_name': script.name,
                        'script_content': script.content,
                    }
                }
            elif action == 'delete':
                res = {
                    'action': action,
                    'data': {
                        'script_id': _id
                    }
                }
            elif action == 'execute':
                execution_log = ExecutionLog.objects.get(id=_id)
                res = {
                    'action': action,
                    'data': {
                        'log_id': _id,
                        'script_id': execution_log.script.id,
                        'execution_started_at': execution_log.execution_started_at,
                        'execution_completed_at': execution_log.execution_completed_at,
                        'execution_time': execution_log.execution_time,
                        'output': execution_log.output,
                    }
                }

            if res:
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    RealTimeConsumer.group_name,
                    {
                        'type': 'mqtt.message',
                        'message': json.dumps(res, cls=CustomJSONEncoder),
                    }
                )

    except json.JSONDecodeError as e:
        print(f'Error decoding JSON: {e}')
        logger.error(f'Error decoding JSON: {e}')


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('topic/script_updates')
    else:
        print('Bad connection. Code:', rc)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
