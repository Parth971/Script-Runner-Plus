from channels.generic.websocket import AsyncWebsocketConsumer


class RealTimeConsumer(AsyncWebsocketConsumer):
    group_name = 'script_updates'

    async def connect(self):
        await self.accept()

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, **kwargs):
        print(f"text_data : {text_data}")
        pass

    async def mqtt_message(self, event):
        # Send MQTT messages to WebSocket clients
        await self.send(event['message'])
