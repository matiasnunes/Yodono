from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Donante

@receiver(post_save, sender=User)
def crear_perfil_donante(sender, instance, created, **kwargs):
    if created:
        Donante.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_donante(sender, instance, **kwargs):
    instance.donante.save()
