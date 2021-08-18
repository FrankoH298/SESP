from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/inicio/', WSConsumer.as_asgi())
]