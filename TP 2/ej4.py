#Ej 4
"""Eliminar de una lista de números enteros aquellos valores que se encuentren en una segunda lista.
    Imprimir la lista original, la lista de valores a eliminar y la lista resultante.
    La función debe modificar la lista original sin crear una copia modificada.    
"""
    
def eliminar_valores(lista_original: list, lista_a_eliminar: list) -> None:
    """recibe dos listas como parámetros, la lista original y la lista de valores a eliminar.
    Elimina de la lista original los valores que se encuentran en la lista de valores a eliminar.
    """
    for valor in lista_a_eliminar:
        while valor in lista_original:
            lista_original.remove(valor)

def main() -> None:
    """
    imprime la lista original y la lista de valores a eliminar. utilizando la función eliminar_valores creamos e imprimimos la lista
    modificada.
    """
    lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_a_eliminar = [2, 4, 6, 8, 10]
    print("Lista original:", lista_original)
    print("Lista de valores a eliminar:", lista_a_eliminar)
    eliminar_valores(lista_original, lista_a_eliminar)
    print("Lista modificada:", lista_original)
    
if  __name__ == "__main__":
    main()
