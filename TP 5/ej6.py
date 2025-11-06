#Ej 6
"""El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def cargar_lista() -> list[int]:
    """
    Carga una lista de números enteros ingresados por el usuario, finalizando con -1.
    """
    lista = []
    while True:
        try:
            n = int(input("Ingrese un número entero (-1 para terminar): "))
            if n == -1:
                break
            lista.append(n)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    return lista


def buscar_en_lista(lista: list[int]) -> None:
    """
    Permite al usuario buscar valores en la lista y muestra la posición de cada uno.
    Finaliza tras tres errores de búsqueda.
    """
    errores = 0
    while errores < 3:
        try:
            valor = int(input("Ingrese un número para buscar su posición: "))
            pos = lista.index(valor)
            print(f"El número {valor} se encuentra en la posición {pos}.")
        except ValueError:
            errores += 1
            print(f"Error: el número no se encuentra en la lista. ({errores}/3)")
    print("Demasiados errores. Proceso finalizado.")


if __name__ == "__main__":
    numeros = cargar_lista()
    if numeros:
        buscar_en_lista(numeros)
    else:
        print("No se cargaron números en la lista.")
