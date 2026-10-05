from datetime import date
def calcular_edad(nacimiento,hoy):
    
    edad = hoy.year - nacimiento.year
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1
    return edad
def _validar_fecha(nacimiento: date, hoy: date) -> None:
    if nacimiento > hoy:
        raise ValueError(ERROR_FECHA_FUTURA)
