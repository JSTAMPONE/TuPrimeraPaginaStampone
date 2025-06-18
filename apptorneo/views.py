from django.shortcuts import render, redirect
from.forms import EquipoForm, JugadorForm, PartidoForm, BusquedaJugadorForm
from.models import Equipo, Jugador, Partido
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio.html')

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return render(request, 'crear_equipo.html', {
                'form': EquipoForm(),
                'mensaje': 'Equipo creado con éxito'
            })
    else: 
        form = EquipoForm() 
    return render(request, 'crear_equipo.html', {'form': form})

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST) 
        if form.is_valid(): 
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            equipo = form.cleaned_data['equipo']
            numero_camiseta = form.cleaned_data['numero_camiseta']
            jugador = Jugador(nombre=nombre, apellido=apellido, equipo=equipo, numero_camiseta=numero_camiseta)
            jugador.save()
            form = JugadorForm() 
            return render(request, 'crear_jugador.html', {'form':form, 'mensaje': 'Jugador creado con éxito'})
        else:
            return render(request, 'crear_jugador.html', {'form': form}) 
    else: 
        form = JugadorForm() 
    return render(request, 'crear_jugador.html', {'form': form})

def crear_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST, request.FILES)
        if form.is_valid(): 
            local = form.cleaned_data['local']
            visitante = form.cleaned_data['visitante']
            fecha = form.cleaned_data['fecha']
            goles_local = form.cleaned_data['goles_local']
            goles_visitante = form.cleaned_data['goles_visitante']
            partido = Partido(local=local, visitante=visitante, fecha=fecha, goles_local=goles_local, goles_visitante=goles_visitante)
            partido.save()
            form = PartidoForm() 
            return render(request, 'crear_partido.html', {'form':form, 'mensaje': 'Partido creado con éxito'})
        else:
            return render(request, 'crear_partido.html', {'form': form}) 
    else: 
        form = PartidoForm() 
    return render(request, 'crear_partido.html', {'form': form})

def buscar_jugador(request):
    if request.method == 'GET':
        form = BusquedaJugadorForm(request.GET)
        if form.is_valid(): 
            nombre = form.cleaned_data['nombre']
            resultados = Jugador.objects.filter(nombre__icontains=nombre)
            return render(request, 'buscar_jugador.html', {'form':form, 'resultados': resultados}) 
    else: 
        form = BusquedaJugadorForm() 
    return render(request, 'buscar_jugador.html', {'form': form})

class PartidoListView(ListView):
    model = Partido
    context_object_name = 'partidos'

class PartidoDetailView(DetailView): 
    model = Partido
    context_object_name = 'detalle_partido'

class PartidoUpdateView(LoginRequiredMixin, UpdateView):
    model = Partido
    fields = ['local', 'visitante', 'fecha', 'goles_local', 'goles_visitante', 'imagen']
    template_name = 'apptorneo/editar_partido.html'
    context_object_name = 'editar_partido'
    success_url = '/'

class PartidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Partido
    template_name = 'apptorneo/partido_confirm_delete.html'
    success_url = reverse_lazy('lista_partidos')

def about(request):
    return render(request, 'apptorneo/about.html')