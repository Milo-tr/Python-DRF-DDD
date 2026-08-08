from dataclasses import dataclass

@dataclass(frozen=True)
class Telefono:
    numero: str

    def __post_init__(self):
        limpio = self.numero.replace(" ", "").replace("-", "").replace("+", "").strip()
        if not limpio.isdigit():
            raise ValueError("El teléfono solo debe contener dígitos")
        object.__setattr__(self, "numero", limpio)

    def __str__(self):
        return self.numero