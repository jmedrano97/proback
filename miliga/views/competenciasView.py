# from rest_framework import viewsets
# from miliga.serializer import  EquiposSerializer
# from miliga.models import  Equipos
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import viewsets
from miliga.serializer import  CompetenciasSerializer
from miliga.models import  Competencias
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CompetenciasViewSet(viewsets.ModelViewSet):
    queryset = Competencias.objects.all()
    serializer_class = CompetenciasSerializer
