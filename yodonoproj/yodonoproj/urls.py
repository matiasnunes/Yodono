"""yodonoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from donantes import views as donantes_views
from solicitudes.views import (
    ListaSolicitudesView,
    DetalleSolicitudView,
    CrearSolicitudView,
)
from solicitudes import views as solicitudes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro_donantes/', donantes_views.registro_donantes, name="registro-donantes"),
    path('datos_donante/', donantes_views.datos_donante, name='datos-donante'),
    path('perfil/', donantes_views.perfil, name='perfil'),
    path('buscar_donantes/', donantes_views.busquedaDonantes, name='buscar-donantes'),
    path('solicitudes/', ListaSolicitudesView.as_view(), name="solicitudes"),
    path('solicitud/<int:pk>', DetalleSolicitudView.as_view(), name="detalle-solicitud"),
    path('solicitud/<int:pk>/participar/', solicitudes_views.participar, name="participar"),
    path('solicitud/nueva/', CrearSolicitudView.as_view(), name="crear-solicitud"),
    path('ingresar/', auth_views.LoginView.as_view(template_name="donantes/ingresar.html"), name='ingresar'),
    path('salir/', auth_views.LogoutView.as_view(template_name="donantes/salir.html"), name='salir'),
    path('', include('inicio.urls')),
]
