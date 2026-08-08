from dataclasses import dataclass
import re 

@dataclass(frozen=True)
class Correo:
    correo: str

    def __post__init__(self):
        correo_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
        if not correo_regex.fullmatch(self.correo):
            raise ValueError("El formato del email es invalido")

    @classmethod
    def _from_db(cls, value: str) -> "Correo":
        """Construye sin validar. Solo para datos que ya persistieron."""
        obj = object.__new__(cls)
        object.__setattr__(obj, "correo", value)
        return obj
    
    def __str__(self):
        return self.correo