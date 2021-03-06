from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .consumers import WSConsumer
from .models import Store, Entry, Exit
from django.contrib.auth.models import User
from .serializers import *

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        if not user.is_superuser:
            Store.objects.create(user = user, name = user.username)

@receiver(post_save, sender=Entry)
def update_store_entries(sender, instance, created, **kwargs):
    if created:
        if not instance.store.is_full:
            instance.store.actual_people += 1
            instance.store.save()
            serializer = StoreSerializer(instance.store)
            WSConsumer.send_data_to_group(instance.store.id, serializer.data)

@receiver(pre_save, sender=Entry)
def update_store_entries(sender, instance, **kwargs):
    if instance.store.is_full:
        raise Exception('Capacidad máxima excedida')

@receiver(post_save, sender=Exit)
def update_store_exits(sender, instance, created, **kwargs):
    if created:
        if instance.store.actual_people > 0:
            instance.store.actual_people -= 1
            instance.store.save()
            serializer = StoreSerializer(instance.store)
            WSConsumer.send_data_to_group(instance.store.id, serializer.data)

@receiver(pre_save, sender=Exit)
def update_store_entries(sender, instance, **kwargs):
    if not instance.store.actual_people > 0:
        raise Exception('Capacidad mínima excedida')

@receiver(post_save, sender=Store)
def update_store(sender, instance, created, **kwargs):
    serializer = StoreSerializer(instance)
    WSConsumer.send_data_to_group(instance.id, serializer.data)
