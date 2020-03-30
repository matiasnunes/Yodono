from django.db import models
from django.contrib.auth.models import User
from donantes.models import Donante
from django.urls import reverse


class Solicitud(models.Model):

    solicitante = models.ForeignKey(Donante, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    edad = models.CharField(max_length=2)
    hospital = models.CharField(max_length=40)
    grupoSanguineo = models.CharField(max_length=11)
    fechaLimite = models.DateField(auto_now=False, auto_now_add=False)
    motivo = models.CharField(max_length=90)
    cantidadDonantes = models.IntegerField()
    departamento = models.CharField(max_length=30)
    participantes = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.fechaLimite}'

    def get_absolute_url(self):
        return reverse('detalle-solicitud', kwargs={'pk': self.pk})

    def calcularDontantesFaltantes(self):
        cant_participantes = self.participantes.count

