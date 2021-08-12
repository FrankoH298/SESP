from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class ShopProfile(models.Model):
    """Model definition for ShopProfile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telephone_number = models.CharField(max_length=100, null=True)
    #address = models.ForeignKey("Address", verbose_name=("Direccion"), on_delete=models.CASCADE, null=True)
    
    class Meta:
        """Meta definition for ShopProfile."""

        verbose_name = 'Perfil del local'
        verbose_name_plural = 'Perfiles de los locales'

    def __str__(self):
        """Unicode representation of ShopProfile."""
        pass


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopProfile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.shopprofile.save()