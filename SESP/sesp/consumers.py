from channels.generic.websocket import WebsocketConsumer
import channels.layers
from asgiref.sync import async_to_sync
import copy, json

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept() # Accept the connection

    def disconnect(self, close_code):
        cant_iteraciones = copy.copy(self.channel_layer.groups)
        for a in cant_iteraciones:
            async_to_sync(self.channel_layer.group_discard)(a, self.channel_name) # Remove all groups
    
    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_add)(text_data, self.channel_name) # Add user to group

    def send_number(self, event):
        self.send(text_data=json.dumps(event['number'])) # Send message to WebSocket
    
    def send_number_to_group(group, text):
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(str(group), {'type': 'send_number', 'number': {"key_id": group, "key_value": text}})