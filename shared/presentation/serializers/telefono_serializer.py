from rest_framework import serializers
from ...infrastructure.django_fields.telefono_field import Telefono
from drf_spectacular.utils import extend_schema_field

@extend_schema_field(serializers.CharField)
class TelefonoSerializer(serializers.Field):

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        try:
            return Telefono(data)
        except ValueError as e:
            raise serializers.ValidationError(str(e))