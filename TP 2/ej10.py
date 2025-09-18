#Ej 10
"""Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla.
"""

import random

def generar_lista_random() -> list:
    """utilizando la biblioteca random, generamos una lista de 20 números al azar
    entre 1 y 100
    """
    return [random.randint(1, 100) for _ in range(20)]

def filtrar_impares(lista: list) -> list:
    """utilizando la función de orden superior filter(), filtramos los elementos impares de la lista
    recibida como parámetro
    """
    return list(filter(lambda x: x % 2 != 0, lista))

def main() -> None:
    """utilizando las funciones previas, generamos una lista  de números al azar y filtramos sus elemntos
    impares, mostrando el resultado en pantalla
    """
    lista_azar = generar_lista_random()
    print("Lista de números al azar:", lista_azar)
    lista_impares = filtrar_impares(lista_azar)
    print("Lista de números impares:", lista_impares)
    
if  __name__ == "__main__":
    main()