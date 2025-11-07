#Ej 6

"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""

import string
from typing import List


def palabras_unicas_ordenadas(frase: str) -> List[str]:
    """
    Recibe una frase, elimina signos de puntuación y palabras repetidas.
    Devuelve una lista de palabras únicas ordenadas por longitud.
    """
    traductor = str.maketrans("", "", string.punctuation)
    limpia = frase.translate(traductor).lower()
    palabras = limpia.split()
    unicas = set(palabras)
    return sorted(unicas, key=len)


def main() -> None:
    frase = input("Ingrese una frase: ").strip()
    resultado = palabras_unicas_ordenadas(frase)
    print("\nPalabras únicas ordenadas por longitud:")
    for palabra in resultado:
        print(palabra)


if __name__ == "__main__":
    main()
