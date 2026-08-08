from shared.domain.value_objects.rut_vo import Rut
from shared.domain.value_objects.correo_vo import Correo
from shared.domain.value_objects.telefono_vo import Telefono
from dataclasses import dataclass

@dataclass()
class Usuario:
    id: str | None
    rut: Rut
    correo: Correo
    telefono: Telefono
    nombre: str
    segundo_nombre: str
    apellido_paterno: str
    apellido_materno: str