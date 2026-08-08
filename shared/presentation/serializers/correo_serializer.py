from rest_framework import serializers
from ...infrastructure.django_fields.correo_field import Correo
from drf_spectacular.utils import extend_schema_field

@extend_schema_field(serializers.CharField)
class CorreoSerializer(serializers.Field):

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        try:
            return Correo(data)
        except ValueError as e:
            raise serializers.ValidationError(str(e))