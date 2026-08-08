from ...infrastructure.models import Usuario
from trabajador.models import Trabajador
from django.db import transaction

class CrearUsuarioConTrabajador:

    @transaction.atomic
    def execute(self, usuario_data: dict) -> tuple[Usuario, Trabajador]:
        usuario = Usuario.objects.create(**usuario_data)
        trabajador = Trabajador.objects.create(
            user=usuario,
            rut=usuario.rut,
            nombre=usuario.nombre,
            segundo_nombre=usuario.segundo_nombre,
            apellido_paterno=usuario.apellido_paterno,
            apellido_materno=usuario.apellido_materno,
            correo=usuario.correo,
            telefono=usuario.telefono,
        )
        return usuario, trabajador