from django.db import models

# Create your models here.
class Ligas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    liga_link = models.CharField(max_length=255, unique=True)
    img_link = models.CharField(max_length=500, null=True, blank=True) 

    class Meta:
        db_table = 'Ligas'
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'

    def __str__(self):
        return self.nombre
    
class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    delegado = models.CharField(max_length=255, null=True, blank=True)
    liga = models.ForeignKey(Ligas, on_delete=models.CASCADE, related_name='equipos')
    created_at = models.DateTimeField(auto_now_add=True)
    img_link = models.CharField(max_length=500, null=True, blank=True)  # Campo de URL de la imagen

    class Meta:
        db_table = 'equipos'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.nombre
    
class Competencias(models.Model):
    PUNTOS = 'Puntos'
    ELIMINATORIA = 'Eliminatoria'
    COMPETENCIAS_TYPE_CHOICES = [
        (PUNTOS, 'Puntos'),
        (ELIMINATORIA, 'Eliminatoria'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    Liga = models.ForeignKey(Ligas, on_delete=models.CASCADE, related_name='competencias')
    created_at = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=255, choices=COMPETENCIAS_TYPE_CHOICES, default=PUNTOS)

    class Meta:
        db_table = 'competencias'
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competencias'

    def __str__(self):
        return self.nombre


class EquiposCompetencias(models.Model):
    id = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, related_name='equipos_competencias')
    competencia = models.ForeignKey(Competencias, on_delete=models.CASCADE, related_name='equipos_competencias')
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'equiposCompetencias'
        verbose_name = 'Equipos Competencias'
        verbose_name_plural = 'Equipos Competencias'
        constraints = [
            models.UniqueConstraint(fields=['equipo', 'competencia'], name='unique_equipo_competencia')
        ]

    def __str__(self):
        return f"{self.equipo.nombre} - {self.competencia.nombre}"