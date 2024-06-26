from rest_framework import viewsets
from miliga.serializer import  CompetenciasSerializer
from miliga.models import  Competencias
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CompetenciasViewSet(viewsets.ModelViewSet):
    queryset = Competencias.objects.all()
    serializer_class = CompetenciasSerializer

@api_view(['GET'])
def CompetenciasByLiga(request, id):
    competencias = Competencias.objects.filter(liga=id)
    serializer = CompetenciasSerializer(competencias, many=True)
    return Response(serializer.data)
