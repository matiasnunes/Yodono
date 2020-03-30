from django import forms
from django.contrib.auth.models import User
from .models import Donante


#class DonanteUpdateForm(forms.ModelForm):
#    grupoSanguineo = forms.CharField(max_length=11)
#
#    class Meta:
#        model = User
#        fields = ['username']


class DonanteDatosForm(forms.ModelForm):

    nombres = forms.CharField(max_length=20)
    apellidos = forms.CharField(max_length=20)
    emailContacto = forms.EmailField(max_length=30)
    numeroContacto = forms.CharField(max_length=12)
    departamento = forms.ChoiceField(choices=Donante.LISTA_DEPARTAMENTOS)
    grupoSanguineo = forms.ChoiceField(choices=Donante.GRUPOS_SANGUINEOS)

    class Meta:
        model = Donante
        fields = ['nombres', 'apellidos', 'emailContacto', 'numeroContacto', 'departamento', 'grupoSanguineo']


