from channels.generic.websocket import WebsocketConsumer
import channels.layers
from asgiref.sync import async_to_sync
import copy, json
from .models import *
from .serializers import *

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept() # Accept the connection
        print("NEW CONNECTION")
        

    def disconnect(self, close_code):
        cant_iteraciones = copy.copy(self.channel_layer.groups)
        for a in cant_iteraciones:
            async_to_sync(self.channel_layer.group_discard)(a, self.channel_name) # Remove all groups
        print("DISCONNECTED")
    def send_data_to_group(group, data):
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(str(group), {'type': 'send_data', 'number': {"key_id": group, "key_value": data}})
        print("SEND_DATA")

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_add)(text_data, self.channel_name) # Add user to group
        print("ADDED TO GROUP {}".format(text_data))
        store = Store.objects.get(pk=text_data)
        serializer = StoreSerializer(store)
        WSConsumer.send_data_to_group(text_data, serializer.data)

    def send_data(self, event):
        self.send(text_data=json.dumps(event['number'])) # Send message to WebSocket
    
    