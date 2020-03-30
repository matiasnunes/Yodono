from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from .models import Solicitud


def ver_solicitudes(request):
    context = {
        'solicitudes': Solicitud.objects.all()
    }
    return render(request, 'solicitudes/solicitudes.html', context)


def participar(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if (solicitud.participantes.count() < solicitud.cantidadDonantes ):
        print('menor')
        solicitud.participantes.add(request.user)
        solicitud.save()
        messages.success(request, f'Usted ha sido añadido como participante a esta solicitud. Gracias!')
    else:
        print('mayor')
    return redirect('detalle-solicitud', pk)


class ListaSolicitudesView(ListView):
    model = Solicitud
    template_name = 'solicitudes/solicitudes.html'
    context_object_name = 'solicitudes'
    ordering = ['fechaLimite']


class DetalleSolicitudView(DetailView):
    model = Solicitud


class CrearSolicitudView(LoginRequiredMixin, CreateView):
    model = Solicitud
    fields = ['nombres','apellidos','edad','hospital','grupoSanguineo',
              'fechaLimite','motivo','cantidadDonantes','departamento']

    def form_valid(self, form):
        form.instance.donante = self.request.user
        return super().form_valid(form)
