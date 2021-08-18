from channels.generic.websocket import WebsocketConsumer
from time import sleep

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()