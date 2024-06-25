from rest_framework import viewsets
from miliga.serializer import  LigasSerializer
from miliga.models import  Ligas

class LigasViewSet(viewsets.ModelViewSet):
    queryset = Ligas.objects.all()
    serializer_class = LigasSerializer