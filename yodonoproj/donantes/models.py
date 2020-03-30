from django.db import models
from django.contrib.auth.models import User


class Donante(models.Model):

    OMENOS = 'O-'
    OMAS = 'O+'
    AMENOS = 'A-'
    AMAS = 'A+'
    BMAS = 'B+'
    BMENOS = 'B-'
    ABMAS = 'AB+'
    ABMENOS = 'AB-'
    DESC= 'Desconocido'


    GRUPOS_SANGUINEOS = [
        ('DESCONOCIDO', 'Desconocido'),
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ]

    LISTA_DEPARTAMENTOS = [
        ('Montevideo', 'Montevideo'),
        ('Artigas', 'Artigas'),
        ('Canelones', 'Canelones'),
        ('Cerro Largo', 'Cerro Largo'),
        ('Colonia', 'Colonia'),
        ('Durazno', 'Durazno'),
        ('Flores', 'Flores'),
        ('Florido', 'Florida'),
        ('Lavalleja', 'Lavalleja'),
        ('Maldonado', 'Maldonado'),
        ('Paysandú', 'Paysandú'),
        ('Rio Negro', 'Rio Negro'),
        ('Rivera', 'Rivera'),
        ('Rocha', 'Rocha'),
        ('Salto', 'Salto'),
        ('San José', 'San José'),
        ('Soriano', 'Soriano'),
        ('Tacuarembó', 'Tacuarembó'),
        ('Treinta y Tres', 'Treinta y Tres')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    emailContacto = models.EmailField(max_length=30)
    numeroContacto = models.CharField(max_length=12)
    departamento = models.CharField(max_length=30, choices=LISTA_DEPARTAMENTOS, default='Montevideo')
    grupoSanguineo = models.CharField(max_length=11, choices=GRUPOS_SANGUINEOS, default='DESC')

    def __str__(self):
        return f'{self.user.username} Donante'

