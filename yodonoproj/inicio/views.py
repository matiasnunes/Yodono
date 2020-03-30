from django.shortcuts import render
from django. http import HttpResponse
from solicitudes.models import Solicitud

def inicio(request):
    context = {
        'solicitudes': Solicitud.objects.all().order_by('fechaLimite')
    }
    return render(request, 'inicio/inicio.html', context)


def informacion(request):
    return render(request, 'inicio/info.html')


def centrosDonacion(request):
    return render(request, 'inicio/centros_donacion.html')
