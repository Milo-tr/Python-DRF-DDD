from django.db import models
import uuid
from shared.infrastructure.django_fields.telefono_field import TelefonoField
from shared.infrastructure.django_fields.correo_field import CorreoField
from shared.infrastructure.django_fields.rut_field import RutField

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, blank=False, null=False, default=uuid.uuid4, editable=False)
    rut = RutField(blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido_paterno = models.CharField(max_length=100, blank=False, null=False)
    apellido_materno = models.CharField(max_length=100, blank=False, null=False)
    correo = CorreoField(blank=False, null=False, unique=True)
    telefono = TelefonoField(blank=False, null=False, unique=False)
    creado_en = models.DateTimeField(auto_now_add=True, null=False)
    actualizado_en = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = 'USUARIO'
        ordering = ['apellido_paterno']
        constraints = [
            models.CheckConstraint(
                check=models.Q(correo__regex=r'^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$'),
                name='usuario_correo_formato_valido',
            ),
        ]