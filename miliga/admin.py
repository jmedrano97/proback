from django.contrib import admin

# Register your models here.

from .models import Ligas, Equipos, Competencias, EquiposCompetencias

admin.site.register(Ligas)
admin.site.register(Equipos)
admin.site.register(Competencias)
admin.site.register(EquiposCompetencias)
