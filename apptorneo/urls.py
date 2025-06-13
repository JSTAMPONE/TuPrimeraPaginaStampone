from django.urls import path
from .views import(
    inicio,
    crear_equipo,
    crear_jugador,
    crear_partido,
    buscar_jugador,
    PartidoListView,
    PartidoDetailView,
    PartidoUpdateView,
    PartidoDeleteView,
    about,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear_equipo/', crear_equipo, name='crear_equipo'),
    path('crear_jugador/', crear_jugador, name='crear_jugador'),
    path('crear_partido/', crear_partido, name='crear_partido'),
    path('buscar_jugador/', buscar_jugador, name='buscar_jugador'),
    path('lista_partidos/', PartidoListView.as_view(), name='lista_partidos'),
    path('partido/<int:pk>/', PartidoDetailView.as_view(), name='detalle_partido'),
    path('editar_partido/<int:pk>/', PartidoUpdateView.as_view(), name='editar_partido'),
    path('borrar_partido/<int:pk>/', PartidoDeleteView.as_view(), name='borrar_partido'),
    path('about/', about, name='about'),
]