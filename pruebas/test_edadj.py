from datetime import date
from edad import calcular_edad  # <--- Esto también causará el fallo esperado

def test_edad_no_cumple_este_anio():
    nacimiento = date(2000, 12, 10)
    hoy = date(2026, 9, 30)
    assert calcular_edad(nacimiento, hoy)


    