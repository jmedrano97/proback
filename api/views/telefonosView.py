from rest_framework import viewsets
from api.serializer import  TelefonosSerializer
from api.models import  Telefonos
from rest_framework.decorators import api_view
from rest_framework.response import Response 

class TelefonosViewSet(viewsets.ModelViewSet):
    queryset = Telefonos.objects.all()
    serializer_class = TelefonosSerializer

@api_view(['GET'])
def telefonosByAlumno(request, id):
    telefonos = Telefonos.objects.filter(alumno=id)
    serializer = TelefonosSerializer(telefonos, many=True)
    return Response(serializer.data)