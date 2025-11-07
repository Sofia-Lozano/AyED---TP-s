#Ej 4

"""Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""

from typing import Tuple

def encajan(ficha1: Tuple[int, int], ficha2: Tuple[int, int]) -> bool:
    """
    Devuelve True si las fichas de dominó encajan (comparten al menos un número).
    """
    return not set(ficha1).isdisjoint(ficha2)


def main() -> None:
    print("=== COMPROBADOR DE FICHAS DE DOMINÓ ===")
    ficha1 = tuple(map(int, input("Ingrese la primera ficha (ej: 3 4): ").split()))
    ficha2 = tuple(map(int, input("Ingrese la segunda ficha (ej: 5 4): ").split()))

    if len(ficha1) != 2 or len(ficha2) != 2:
        print("Error: cada ficha debe tener exactamente dos valores.")
        return

    if encajan(ficha1, ficha2):
        print("Las fichas encajan.")
    else:
        print("Las fichas no encajan.")


if __name__ == "__main__":
    main()
