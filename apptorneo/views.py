from django.shortcuts import render, redirect
from.forms import EquipoForm, JugadorForm, PartidoForm, BusquedaJugadorForm
from.models import Equipo, Jugador, Partido
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio.html')

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST) 
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Equipo creado con éxito')
            return redirect('crear_equipo')
    else: 
        form = EquipoForm() 
    return render(request, 'crear_equipo.html', {'form': form})

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST) 
        if form.is_valid(): 
            jugador = form.save()
            messages.success(request, 'Jugador creado con éxito')
            return redirect('crear_jugador')
    else:
        form = JugadorForm()
    return render(request, 'crear_jugador.html', {'form': form})

def crear_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Partido creado con éxito')
            return redirect('crear_partido')
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
    form_class = PartidoForm
    template_name = 'apptorneo/editar_partido.html'
    context_object_name = 'editar_partido'
    success_url = '/'

class PartidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Partido
    template_name = 'apptorneo/partido_confirm_delete.html'
    success_url = reverse_lazy('lista_partidos')

def about(request):
    return render(request, 'apptorneo/about.html')