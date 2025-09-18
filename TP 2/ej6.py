#Ej 6
"""Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas
que cada elemento tiene en la lista original.
Desarrollar también un programa que permita verificar el comportamiento de la función. Por ejemplo, 
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
def normalizar(lista: list) -> list:
    """normaliza la lista recibida como parámetro
    """
    suma_total = sum(lista)
    return [elemento / suma_total for elemento in lista]

def main() -> None:
    lista1 = [1, 1, 2]
    lista2 = [3, 3, 3]
    lista3 = [10, 20, 30]
    
    print("Lista 1:", lista1, "Normalizada:", normalizar(lista1))
    print("Lista 2:", lista2, "Normalizada:", normalizar(lista2))
    print("Lista 3:", lista3, "Normalizada:", normalizar(lista3))
    
if  __name__ == "__main__":
    main()
