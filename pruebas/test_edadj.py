from datetime import date
import pytest
from edad import calcular_edad

# --- CICLO 1 & 2: Casos Normales y Cumpleaños Pendiente ---
def test_edad_no_cumple_este_anio():
    nacimiento = date(2000, 12, 10)
    hoy = date(2026, 9, 30)
    assert calcular_edad(nacimiento, hoy) == 25

def test_edad_el_dia_del_cumpleanios():
    nacimiento = date(2000, 9, 30)
    hoy = date(2026, 9, 30)
    assert calcular_edad(nacimiento, hoy) == 26
    
def test_fecha_nacimiento_futura_lanza_excepcion():
    with pytest.raises(ValueError, match="La fecha de nacimiento no puede ser posterior a la fecha actual"):
        calcular_edad(date(2027, 1, 1), date(2026, 9, 30))

