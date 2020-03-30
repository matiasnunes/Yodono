from django.contrib import admin
from django.urls import path
from . import views as inicio_views
from donantes import views as registro_views
from solicitudes.views import ListaSolicitudesView

urlpatterns = [
    path('', inicio_views.inicio, name='inicio'),
    path('informacion/', inicio_views.informacion, name='informacion'),
    path('centros_donacion/', inicio_views.centrosDonacion, name='centros-donacion'),
]
