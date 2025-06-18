from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.utils import timezone

class Equipo(models.Model):
    nombre= models.CharField(max_length=30)
    año_fundacion= models.IntegerField()
    
    def clean(self):
        super().clean()

        if self.año_fundacion > timezone.now().year:
            raise ValidationError({'año_fundacion': 'El año de fundación no puede ser en el futuro.'})

        if Equipo.objects.exclude(pk=self.pk).filter(
            nombre__iexact=self.nombre,
            año_fundacion=self.año_fundacion
        ).exists():
            raise ValidationError('Ya existe un equipo con ese nombre y año de fundación.')
            
    def __str__(self):
            return f"{self.nombre} {self.año_fundacion}"
    

class Jugador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)
    numero_camiseta= models.IntegerField(
          validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    def __str__(self):
            return f"{self.nombre} {self.apellido} {self.equipo} {self.numero_camiseta}"

class Partido(models.Model):
    local= models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    visitante= models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    fecha= models.DateTimeField()
    goles_local= models.IntegerField()
    goles_visitante= models.IntegerField()
    imagen = models.ImageField(upload_to='partidos', null=True, blank=True)
    descripcion = RichTextField(blank=True, null=True)

    def __str__(self):
            return f"{self.local.nombre} vs {self.visitante.nombre} {self.fecha.strftime('%d/%m/%Y %H:%M')} {self.goles_local}:{self.goles_visitante}"
    