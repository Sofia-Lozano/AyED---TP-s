#Ej 2
"""Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo
números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""

def sumar_cadenas(cadena1: str, cadena2: str) -> float:
    """
    Recibe dos cadenas que representan números reales.
    Devuelve la suma como número real o -1 si alguna cadena no es válida.
    """
    try:
        num1 = float(cadena1)
        num2 = float(cadena2)
        return num1 + num2
    except ValueError:
        return -1


if __name__ == "__main__":
    c1 = input("Ingrese el primer número: ")
    c2 = input("Ingrese el segundo número: ")
    resultado = sumar_cadenas(c1, c2)
    if resultado == -1:
        print("Error: al menos una de las cadenas no es un número válido.")
    else:
        print(f"Resultado de la suma: {resultado}")
