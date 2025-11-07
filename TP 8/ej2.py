#Ej 2

"""Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""

from typing import Tuple

def fecha_en_texto(fecha: Tuple[int, int, int], anio_corte: int = 30) -> str:
    """
    Convierte una fecha (día, mes, año) en formato extendido.
    Si el año tiene 2 dígitos, usa el año de corte para decidir el siglo.
    """
    dia, mes, anio = fecha
    if anio < 100:
        if anio <= anio_corte:
            anio += 2000
        else:
            anio += 1900

    nombres_meses = (
        "", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )

    if not (1 <= mes <= 12):
        raise ValueError("Mes inválido.")

    return f"{dia} de {nombres_meses[mes]} de {anio}"


def main() -> None:
    print("=== FECHA EN FORMATO EXTENDIDO ===")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anio = int(input("Año (2 o 4 dígitos): "))
    fecha = (dia, mes, anio)
    try:
        print(fecha_en_texto(fecha))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
