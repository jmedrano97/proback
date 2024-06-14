from django.db import models

class Alumnos(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    # Dirección
    avenida_calle = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    alcaldia_municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'


class Telefonos(models.Model):
    alumno = models.ForeignKey(Alumnos, related_name='telefonos', on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.alumno.nombres} - {self.numero}'
