from channels.generic.websocket import WebsocketConsumer
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
        async_to_sync(self.channel_layer.group_send)("1", {'type': 'send_number', 'number': 1})

    def send_number(self, event):
        self.send(text_data=json.dumps(event['number'])) # Send message to WebSocket