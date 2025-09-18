#Ej 5
"""Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función.
"""

def ordenada(lista: list) -> bool:
    """comprobamos si la lista otorgada como parámetro
    está o no ordenada en forma ascendente, retornamos booleanos.
    """
    return lista == sorted(lista)

def main() -> None:
    """
    utilizando la función  ordenada, comprobamos si las listas otorgadas como parámetros están ordenadas
    en forma ascendente.
    """
    lista1 = [1, 2, 3]
    lista2 = ['b', 'a']
    lista3 = [1, 1, 1]
    lista4 = [3, 2, 1]
    
    print("Lista 1:", lista1, "Ordenada:", ordenada(lista1))
    print("Lista 2:", lista2, "Ordenada:", ordenada(lista2))
    print("Lista 3:", lista3, "Ordenada:", ordenada(lista3))
    print("Lista 4:", lista4, "Ordenada:", ordenada(lista4))
    
if __name__ == "__main__":
    print (main())