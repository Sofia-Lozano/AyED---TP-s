#Ej 1

"""Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""

from datetime import date, timedelta, datetime
from typing import Tuple


def ingresar_fecha() -> Tuple[int, int, int]:
    """
    Solicita una fecha válida desde teclado y la devuelve como tupla (día, mes, año).
    """
    while True:
        try:
            dias = int(input("Día: "))
            mes = int(input("Mes: "))
            anio = int(input("Año: "))
            date(anio, mes, dias)  
            return dias, mes, anio
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")


def sumar_dias(fecha: Tuple[int, int, int], n: int) -> Tuple[int, int, int]:
    """
    Suma n días a una fecha dada y devuelve la nueva fecha como tupla.
    """
    dia, mes, anio = fecha
    nueva = date(anio, mes, dia) + timedelta(days=n)
    return nueva.day, nueva.month, nueva.year


def ingresar_horario() -> Tuple[int, int, int]:
    """
    Solicita un horario válido desde teclado y lo devuelve como tupla (hora, minuto, segundo).
    """
    while True:
        try:
            hora = int(input("Hora (0-23): "))
            minuto = int(input("Minuto (0-59): "))
            segundo = int(input("Segundo (0-59): "))
            if not (0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60):
                raise ValueError
            return hora, minuto, segundo
        except ValueError:
            print("Horario inválido. Intente nuevamente.")


def diferencia_horarios(horario1: Tuple[int, int, int], horario2: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    Calcula la diferencia entre dos horarios.
    Si h1 > h2, se considera que h1 pertenece al día anterior.
    Devuelve una tupla (horas, minutos, segundos).
    """
    t1 = datetime(2000, 1, 1, horario1[0], horario1[1], horario1[2])
    t2 = datetime(2000, 1, 1, horario2[0], horario2[1], horario2[2])
    if t1 > t2:
        t2 += timedelta(days=1)
    dif = t2 - t1
    if dif.total_seconds() > 86400:
        raise ValueError("La diferencia no puede superar las 24 horas.")
    segundos = int(dif.total_seconds())
    hora = segundos // 3600
    minuto = (segundos % 3600) // 60
    segundo = segundos % 60
    return hora, minuto, segundo


def main() -> None:
    print("=== MANEJO DE FECHAS Y HORARIOS ===")
    fecha = ingresar_fecha()
    n = int(input("Días a sumar: "))
    nueva_fecha = sumar_dias(fecha, n)
    print(f"Fecha original: {fecha[0]:02d}/{fecha[1]:02d}/{fecha[2]}")
    print(f"Fecha resultante: {nueva_fecha[0]:02d}/{nueva_fecha[1]:02d}/{nueva_fecha[2]}")

    print("\n--- Diferencia entre horarios ---")
    print("Primer horario:")
    horario1 = ingresar_horario()
    print("Segundo horario:")
    horario2 = ingresar_horario()
    dif = diferencia_horarios(horario1, horario2)
    print(f"Diferencia: {dif[0]} horas, {dif[1]} minutos, {dif[2]} segundos")


if __name__ == "__main__":
    main()
