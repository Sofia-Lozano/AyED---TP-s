#Ej 5

"""En geometría un vector es un segmento de recta orientado que va desde un punto
A hasta un punto B. Los vectores en el plano se representan mediante un par ordenado
de números reales (x, y) llamados componentes. Para representarlos basta
con unir el origen de coordenadas con el punto indicado en sus componentes:Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo
basta calcular su producto escalar y verificar si es igual a 0. Ejemplo:A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función.
"""

from typing import Tuple

def son_octogonales(v1: Tuple[float, float], v2: Tuple[float, float]) -> bool:
    """
    Devuelve True si los vectores v1 y v2 son octogonales (su producto escalar es 0).
    """
    producto = v1[0] * v2[0] + v1[1] * v2[1]
    return abs(producto) < 1e-9  # tolerancia para decimales


def main() -> None:
    print("=== COMPROBADOR DE VECTORES OCTOGONALES ===")
    x1, y1 = map(float, input("Ingrese el primer vector (x y): ").split())
    x2, y2 = map(float, input("Ingrese el segundo vector (x y): ").split())

    if son_octogonales((x1, y1), (x2, y2)):
        print("Los vectores son octogonales.")
    else:
        print("Los vectores no son octogonales.")


if __name__ == "__main__":
    main()
