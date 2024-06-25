from django.contrib import admin

# Register your models here.

from .models import Ligas, Equipos, Competencias, EquipoCompetencia

admin.site.register(Ligas)
admin.site.register(Equipos)
admin.site.register(Competencias)
admin.site.register(EquipoCompetencia)
