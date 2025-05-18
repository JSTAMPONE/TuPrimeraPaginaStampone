from django.urls import path
from .views import inicio
from .views import crear_equipo
from .views import crear_jugador
from .views import crear_partido
from .views import buscar_jugador

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear_equipo/', crear_equipo, name='crear_equipo'),
    path('crear_jugador/', crear_jugador, name='crear_jugador'),
    path('crear_partido/', crear_partido, name='crear_partido'),
    path('buscar_jugador/', buscar_jugador, name='buscar_jugador'),
]