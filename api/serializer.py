from rest_framework import serializers, status
from .models import Alumnos, Telefonos
class TelefonosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefonos
        fields = '__all__'

class AlumnosSerializer(serializers.ModelSerializer):
    telefonos = TelefonosSerializer(many=True, read_only=True)
    class Meta:
        model = Alumnos
        fields = '__all__'
