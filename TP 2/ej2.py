#Ej 2
""". Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa.
"""

#A
import random

def generar_lista() -> list:
    n = int(input("Ingrese un número entero: "))
    lista = [random.randint(1, 100) for _ in range(n)]
    return lista

#B
def contiene_duplicados(lista: list) -> bool:
    """utilizando la función set, comprobamos si la lista tiene elementos repetidos,
    devuelve booleanos
    """
    return len(lista) != len(set(lista))

#C
def elementos_unicos(lista: list) -> list:
    """recibimos una lista como parámetro y utilizando la función set, devolvemos una nueva lista
    sin elementos repetidos.
    """
    return list(set(lista))

def main() -> None:
    """
    utilizando las funciones anteriores, creamos una lista con n elementos aleatorios, comprobamos si contiene elementos
    duplicados y creamos una nueva lista con los elementos únicos.
    """
    lista = generar_lista()
    print("Lista original:", lista)
    
    if contiene_duplicados(lista):
        print("La lista contiene duplicados.")
    else:
        print("La lista no contiene duplicados.")
    
    lista_unicos = elementos_unicos(lista)
    print("Lista de elementos únicos:", lista_unicos)
    
if __name__ ==  "__main__":
    main()

