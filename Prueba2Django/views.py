from django.shortcuts import redirect, render
from Prueba2Django.forms import FormSeminario
from Prueba2Django.models import Seminario

def index(request):
    return(render(request, 'index.html'))

def seminario_list(request):
    reservas = Seminario.objects.all()
    data = {'reservas': reservas}
    return(render(request, 'reserva.html', data))

def seminario_add(request):
    form = FormSeminario()
    if request.method == 'POST':
        form = FormSeminario(request.POST)
        if form.is_valid():
            reserva = Seminario()
            reserva.nombre = form.cleaned_data['nombre']
            reserva.telcontacto = form.cleaned_data['telcontacto']
            reserva.fechaseminario = form.cleaned_data['fechaseminario']
            reserva.empresa = form.cleaned_data['empresa']
            reserva.email = form.cleaned_data['email']
            reserva.profesion = form.cleaned_data['profesion']
            reserva.observacion = form.cleaned_data['observacion']
            reserva.save()
            return index(request)
    data = {'form': form}
    return(render(request, 'addreserva.html', data))

def seminario_delete(request, id):
    reserva = Seminario.objects.get(id=id)
    reserva.delete()
    return(redirect('/lista'))

def seminario_mod(request, id):
    reserva = Seminario.objects.get(id=id)
    form = FormSeminario(instance=reserva)

    if request.method == 'POST':
        form = FormSeminario(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return(render(request, 'addreserva.html', data))
