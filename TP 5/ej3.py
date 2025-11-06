#Ej 3
"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""

def nombre_mes(numero_mes: int) -> str:
    """
    Devuelve el nombre del mes correspondiente al número recibido (1-12).
    Retorna una cadena vacía si el número es inválido.
    """
    try:
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        if numero_mes < 1 or numero_mes > 12:
            raise IndexError("Número de mes fuera de rango.")
        return meses[numero_mes - 1]
    except (TypeError, IndexError):
        return ""


if __name__ == "__main__":
    try:
        num = int(input("Ingrese el número del mes (1-12): "))
        print(f"Mes: {nombre_mes(num)}")
    except ValueError:
        print("Entrada inválida: debe ingresar un número entero.")
