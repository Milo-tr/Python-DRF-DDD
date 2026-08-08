from django.db import models
from ...domain.value_objects.telefono_vo import Telefono

class TelefonoField(models.CharField):
    description = "Value Object Telefono"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 20)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return Telefono(numero=value)

    def to_python(self, value):
        if isinstance(value, Telefono) or value is None:
            return value
        return Telefono(numero=value)

    def get_prep_value(self, value):
        if isinstance(value, Telefono):
            return value.numero
        return value

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return str(value) if value is not None else value