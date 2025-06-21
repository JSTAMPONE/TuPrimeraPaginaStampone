from django import forms 
from .models import Equipo, Jugador, Partido

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('nombre', 'año_fundacion')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'año_fundacion': forms.NumberInput(attrs={'class': 'form-control'}),
        }

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
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'equipo': forms.Select(attrs={'class': 'form-control'}),
            'numero_camiseta': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ('local', 'visitante', 'fecha', 'goles_local', 'goles_visitante', 'imagen', 'descripcion')
        widgets = {
            'local': forms.Select(attrs={'class': 'form-control'}),
            'visitante': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}, format='%Y-%m-%dT%H:%M'),
            'goles_local': forms.NumberInput(attrs={'class': 'form-control'}),
            'goles_visitante': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class BusquedaJugadorForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre del jugador',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )