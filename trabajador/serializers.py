from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Trabajador
from shared.presentation.serializers.telefono_serializer import TelefonoSerializer
from shared.presentation.serializers.rut_serializer import RutSerializer
from shared.presentation.serializers.correo_serializer import CorreoSerializer

class TrabajadorSerializer(serializers.ModelSerializer):
    telefono = TelefonoSerializer()
    rut = RutSerializer(validators=[UniqueValidator(queryset=Trabajador.objects.all())])
    correo = CorreoSerializer(validators=[UniqueValidator(queryset=Trabajador.objects.all())])

    class Meta:
        model = Trabajador
        fields = '__all__'
        read_only_fields = ['id', 'creado_en', 'actualizado_en']