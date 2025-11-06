#Ej 7

"""Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número
que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""

import random

def jugar_adivinanza() -> None:
    """
    Genera un número aleatorio entre 1 y 500 y permite al usuario adivinarlo.
    Informa si el número buscado es mayor o menor y cuenta los intentos,
    incluyendo los ingresos no válidos.
    """
    numero_secreto = random.randint(1, 500)
    intentos = 0

    print("Adivine el número (entre 1 y 500):")

    while True:
        try:
            intento = input("Ingrese su número: ").strip()
            intentos += 1
            numero = int(intento)

            if numero < numero_secreto:
                print("El número secreto es mayor.")
            elif numero > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Correcto! Adivinó el número en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")


if __name__ == "__main__":
    jugar_adivinanza()
