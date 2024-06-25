from rest_framework import viewsets
from miliga.serializer import  EquiposSerializer
from miliga.models import  Equipos
from rest_framework.decorators import api_view
from rest_framework.response import Response

class EquiposViewSet(viewsets.ModelViewSet):
    queryset = Equipos.objects.all()
    serializer_class = EquiposSerializer
    