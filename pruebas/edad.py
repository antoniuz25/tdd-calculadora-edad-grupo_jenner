from datetime import date

ERROR_FECHA_FUTURA = "La fecha de nacimiento no puede ser posterior a la fecha actual"

def calcular_edad(nacimiento: date, hoy: date) -> int:
    _validar_fecha(nacimiento, hoy)
    
    edad = hoy.year - nacimiento.year
    if not _ya_cumplio_anios(nacimiento, hoy):
        edad -= 1
    return edad

def _validar_fecha(nacimiento: date, hoy: date) -> None:
    if nacimiento > hoy:
        raise ValueError(ERROR_FECHA_FUTURA)

def _ya_cumplio_anios(nacimiento: date, hoy: date) -> bool:
    return (hoy.month, hoy.day) >= (nacimiento.month, nacimiento.day)
