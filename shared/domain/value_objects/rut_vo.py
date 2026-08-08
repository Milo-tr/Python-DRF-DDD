from dataclasses import dataclass

@dataclass(frozen=True)
class Rut:
    rut: str

    def __post__init__(self):
        rut_limpio =  self.rut.replace(".", "").replace("-", "").strip()
        rut_cuerpo = rut_limpio[:-1]
        rut_dv = rut_limpio[-1].upper()

        if not rut_cuerpo.isdigit() or not (1 <= len(rut_cuerpo) <= 8):
            raise ValueError("Cuerpo del RUT no es valido")
            
        if rut_dv not in '0123456789K':
            raise ValueError("Digito verificador no valido")

        suma = 0
        mult = 2

        for i in reversed(rut_cuerpo):
            suma += int(i) * mult
            mult = 2 if mult == 7 else mult + 1

        resto = 11 - (suma % 11)

        if resto == 11:
            dv_esperado = '0'
        elif resto == 10:
            dv_esperado = 'K'
        else:
            dv_esperado = str(resto)

        if rut_dv != dv_esperado:
            raise ValueError(f"Dígito verificador inválido: se esperaba {dv_esperado}, se recibió {rut_dv}")

        object.__setattr__(self, "rut", f"{rut_cuerpo}-{rut_dv}")

    def __str__(self):
            return self.rut