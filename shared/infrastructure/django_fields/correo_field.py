from django.db import models
from ...domain.value_objects.correo_vo import Correo

class CorreoField(models.CharField):
    description = "Value Object Correo"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 100)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return Correo(correo=value)

    def to_python(self, value):
        if isinstance(value, Correo) or value is None:
            return value
        return Correo(correo=value)

    def get_prep_value(self, value):
        if isinstance(value, Correo):
            return value.correo
        return value

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return str(value) if value is not None else value