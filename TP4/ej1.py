#Ej 1
"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""
def es_capicua(cadena: str) -> bool:
    """verifica si la cadena brindada por el usuario es capicúa o no, retorna booleanos.
    """
    lista = list(cadena)
    for x in range(len(lista)):
        if lista[x] != lista[len(lista) - x -1]:
            return False
    return True

def main() -> None:
    """solicita al usuario una cadena de caracteres y lo valida utilizando la función es_capicua,
    muestra el resultado en pantalla
    """
    cadena = input("Ingrese una cadena de caracteres: ")
    if es_capicua(cadena):
        print(f"La cadena {cadena} es capicúa.")
    else:
        print(f"La cadena {cadena} no es capicúa.")
        
if  __name__ == "__main__":
    main()
