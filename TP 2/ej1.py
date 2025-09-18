#Ej 1
"""Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""

#A
import random

def cargar_lista() -> list:
    """cargamos una lista con números al azar utilizando la biblioteca random
    """
    num_elementos = random.randint(10, 99) 
    lista = [random.randint(1000, 9999) for _ in range(num_elementos)]
    return lista

#B
def calcular_producto(lista: list) -> int:
    """calculamos el producto de los elementos enteros de una lista 
    """
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

#C
def eliminar_valor(lista: list, valor: int) -> None:
    """recibimos un valor como parámetro y si se encuentra en la lista, se eliminan todas
    sus apariciones
    """
    while valor in lista:
        lista.remove(valor)
        
#D
def es_capicua(lista: list) -> bool:
    """compara una lista con su versión espejada para determinar si es capicúa, retona True si lo es y False en caso contrario.
    """
    return lista == lista[::-1]  


def main() -> None:
    """Utilizando las funciones previas, creamos y cargamos una lista con valores al azar, calculamos su producto,
    solicitamos al usuario un valor y lo eliminamos si se encuentra en la lista, y finalmente determinamos si la lista
    es capicúa.
    """
    lista = cargar_lista()
    print("Lista original:", lista)
    
    producto = calcular_producto(lista)
    print("Producto de los elementos:", producto)
    
    valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
    eliminar_valor(lista, valor_a_eliminar)
    print("Lista después de eliminar el valor:", lista)
    
    es_capicua_lista = es_capicua(lista)
    print("La lista es capicúa" if es_capicua_lista else "La lista no es capicúa")
    
if __name__ == "__main__":
    main()
