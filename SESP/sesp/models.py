from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.fields import CharField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import admin
from .consumers import WSConsumer

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=100, null=True)
    max_people = models.SmallIntegerField(default=0) # Default 0 porque a la hora de crear un user es nulo y no puede calcular is_full
    actual_people = models.SmallIntegerField(default=0)
    #address = models.ForeignKey("Address", verbose_name=("Direccion"), on_delete=models.CASCADE, null=True)

    @property
    def is_full(self):
        return self.actual_people >= self.max_people

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.name


class Action(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self, action):
        return (f"{action} at: {self.datetime} in {self.store.name}'s store")


class Entry(Action):
    
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return super().__str__('Entry')


class Exit(Action):

    class Meta:
        verbose_name = 'Exit'
        verbose_name_plural = 'Exits'

    def __str__(self):
        return super().__str__('Exit')


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
        instance.store.actual_people -= 1
        instance.store.save()
        WSConsumer.send_number_to_group(1, instance.store.actual_people)