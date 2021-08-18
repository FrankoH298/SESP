from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.fields import CharField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import admin

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=100, null=True)
    max_people = models.SmallIntegerField()
    #address = models.ForeignKey("Address", verbose_name=("Direccion"), on_delete=models.CASCADE, null=True)
    
    @property
    def actual_people(self): #Geteo de todas las instancias, poco eficaz, posible eliminacion
        entries = len(Entry.objects.filter(store=self))
        exits = len(Exit.objects.filter(store=self))
        # Si me da negativo (hubo entradas no notificadas) devuelvo 0 para evitar errores
        actual_people = entries - exits
        if actual_people < 0:
            actual_people = 0

        return actual_people

    @property
    def is_full(self):  # Geteo de todas las instancias, poco eficaz, posible eliminacion
        return self.actual_people >= self.max_people

    class Meta:
        verbose_name = 'Perfil del local'
        verbose_name_plural = 'Perfiles de los locales'

    def __str__(self):
        return self.name


class Action(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self, action):
        return (f"{action} at: {self.datetime} in {self.store.name}'s store")


class Entry(Action):
    
    def __str__(self):
        return super().__str__('Entry')

    class Meta:
        verbose_name_plural = 'Entries'


class Exit(Action):

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