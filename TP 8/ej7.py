#Ej 7

"""Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido
del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""

def main() -> None:
    """
    Crea un conjunto con números del 0 al 9 y permite al usuario eliminar elementos.
    Finaliza al ingresar -1. Muestra el conjunto luego de cada eliminación.
    """
    numeros = set(range(10))

    while True:
        try:
            valor = int(input("Ingrese un número a eliminar (-1 para salir): "))
            if valor == -1:
                break
            numeros.remove(valor)
            print(f"Elemento {valor} eliminado. Conjunto actual: {numeros}")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
        except KeyError:
            print("El número no se encuentra en el conjunto.")

    print(f"\nProceso finalizado. Conjunto final: {numeros}")


if __name__ == "__main__":
    main()
