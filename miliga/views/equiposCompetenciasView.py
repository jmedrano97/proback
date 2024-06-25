from rest_framework import viewsets
from miliga.serializer import  EquiposCompetenciasSerializer
from miliga.models import  EquiposCompetencias
from rest_framework.decorators import api_view
from rest_framework.response import Response

class EquiposCompetenciasViewSet(viewsets.ModelViewSet):
    queryset = EquiposCompetencias.objects.all()
    serializer_class = EquiposCompetenciasSerializer
