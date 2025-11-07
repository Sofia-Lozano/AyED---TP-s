#Ej 8

"""Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""

def main() -> None:
    """
    Genera un diccionario con claves de 1 a 20 y valores iguales al cuadrado de las claves.
    """
    cuadrados = {n: n ** 2 for n in range(1, 21)}

    print("Diccionario de cuadrados:")
    for clave, valor in cuadrados.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
