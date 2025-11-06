#Ej 5
"""La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""

import math

def calcular_raiz_cuadrada() -> None:
    """
    Solicita un número al usuario y muestra su raíz cuadrada.
    Controla errores si el valor ingresado no es numérico o es negativo.
    """
    try:
        valor = float(input("Ingrese un número: "))
        if valor < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        print(f"La raíz cuadrada de {valor} es {math.sqrt(valor)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    calcular_raiz_cuadrada()
