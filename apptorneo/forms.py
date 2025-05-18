from django import forms 
from .models import Equipo
from .models import Jugador
from.models import Partido

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('nombre', 'año_fundacion')

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ('nombre', 'apellido', 'equipo', 'numero_camiseta')

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ('local', 'visitante', 'fecha', 'goles_local', 'goles_visitante')
        widgets={'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')}

class BusquedaJugadorForm(forms.Form):
    nombre= forms.CharField()