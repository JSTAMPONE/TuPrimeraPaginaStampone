from django.shortcuts import render
from.forms import EquipoForm
from.models import Equipo
from.forms import JugadorForm
from.models import Jugador
from.forms import PartidoForm
from.models import Partido
from.forms import BusquedaJugadorForm

def inicio(request):
    return render(request, 'inicio.html')

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST) 
        if form.is_valid(): 
            nombre = form.cleaned_data['nombre'] 
            año_fundacion = form.cleaned_data['año_fundacion']
            equipo = Equipo(nombre=nombre, año_fundacion=año_fundacion)
            equipo.save()
            form = EquipoForm() 
            return render(request, 'crear_equipo.html', {'form':form, 'mensaje': 'Equipo creado con éxito'})
        else:
            return render(request, 'crear_equipo.html', {'form': form}) 
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
        form = PartidoForm(request.POST) 
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