from django import forms 
from .models import Equipo, Jugador, Partido

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('nombre', 'año_fundacion')

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ('nombre', 'apellido', 'equipo', 'numero_camiseta')
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'equipo': 'Equipo',
            'numero_camiseta': 'Número de camiseta',
        }
        error_messages = {
            'numero_camiseta': {
                'min_value': 'El número debe ser al menos 1.',
                'max_value': 'El número no puede ser mayor a 99.',
                'invalid': 'Ingrese un número válido.',
            },
        }

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ('local', 'visitante', 'fecha', 'goles_local', 'goles_visitante', 'imagen', 'descripcion')
        widgets={'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')}

class BusquedaJugadorForm(forms.Form):
    nombre= forms.CharField()