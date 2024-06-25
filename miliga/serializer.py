from rest_framework import serializers, status
from .models import Ligas, Equipos, Competencias, EquiposCompetencias

class LigasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligas
        fields = '__all__'

class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipos
        fields = '__all__'

class CompetenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencias
        fields = '__all__'

class EquiposCompetenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquiposCompetencias
        fields = '__all__'

        