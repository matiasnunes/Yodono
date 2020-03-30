#from django.contrib.auth.models import User
from .models import Donante
import django_filters

class FiltroDonantes(django_filters.FilterSet):
    class Meta:
        model = Donante
        fields = ['departamento', 'grupoSanguineo']