from django.dispatch import receiver
from django.db.models.signals import post_save
from .consumers import WSConsumer
from .models import Store, Entry, Exit
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Store.objects.create(user = user, name = user.username)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.store.save()

@receiver(post_save, sender=Entry)
def update_store_entries(sender, instance, created, **kwargs):
    if created:
        if not instance.store.is_full:
            instance.store.actual_people += 1
            instance.store.save()
            WSConsumer.send_number_to_group(1, instance.store.actual_people)

@receiver(post_save, sender=Exit)
def update_store_exits(sender, instance, created, **kwargs):
    if created:
        if instance.store.actual_people > 0:
            instance.store.actual_people -= 1
            instance.store.save()
            WSConsumer.send_number_to_group(1, instance.store.actual_people)