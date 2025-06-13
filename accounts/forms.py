from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Mensaje

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'cuerpo']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_receptor(self):
        receptor = self.cleaned_data.get('receptor')
        if receptor == self.user:
            raise forms.ValidationError("No podés enviarte un mensaje a vos mismo.")
        return receptor
