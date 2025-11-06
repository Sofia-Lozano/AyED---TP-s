#Ej 1
"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""
def es_capicua(cadena: str) -> bool:
    """verifica si la cadena brindada por el usuario es capicúa o no, retorna booleanos.
    """
    x, y = 0, len(cadena) - 1
    while x < y:
        if cadena[x] != cadena[y]:
            return False
        x += 1
        y -= 1
    return True

def main() -> None:
    """solicita al usuario una cadena de caracteres y lo valida utilizando la función es_capicua,
    muestra el resultado en pantalla
    """
    cadena = input("Ingrese una cadena de caracteres: ")
    if es_capicua(cadena):
        print("La cadena es capicúa.")
    else:
        print("La cadena no es capicúa.")
        
if  __name__ == "__main__":
    main()
