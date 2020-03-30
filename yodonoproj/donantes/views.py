from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import DonanteDatosForm
from django.contrib.auth.decorators import login_required
from .filter import FiltroDonantes
from .models import Donante


def registro_donantes(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}. Ahora puede ingresar al sistema.')

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, user)
            return redirect('datos-donante')
    else:
        form = UserCreationForm()
    return render(request, 'donantes/registro_donante.html', {'form': form})


@login_required
def datos_donante(request):

    if request.method == 'POST':
        donante_form = DonanteDatosForm(request.POST, instance=request.user.donante)
        if donante_form.is_valid():
            donante_form.save()
            messages.success(request, f'Datos actualizados! Muchas gracias.')
            return redirect('perfil')
    else:
        donante_form = DonanteDatosForm()

    context = {
        'donante_form': donante_form
    }
    return render(request, 'donantes/datos_donante.html', context)

@login_required
def perfil(request):
    return render(request, 'donantes/perfil.html')


def busquedaDonantes(request):
    lista_donantes = Donante.objects.all()
    filtro_donantes = FiltroDonantes(request.GET, queryset=lista_donantes)
    return render(request, 'donantes/buscar_donante.html', {'filtro': filtro_donantes})
