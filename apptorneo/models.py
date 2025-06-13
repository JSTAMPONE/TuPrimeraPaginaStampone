from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Equipo(models.Model):
    nombre= models.CharField(max_length=30)
    año_fundacion= models.IntegerField()
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

    def __str__(self):
            return f"{self.local.nombre} vs {self.visitante.nombre} {self.fecha.strftime('%d/%m/%Y %H:%M')} {self.goles_local}:{self.goles_visitante}"
    