#Ej 7
"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres
dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

#A

def eliminar_con_slices(cadena: str, posicion: int, cantidad: int) -> str:
    """recibe una  cadena, una posición y una cantidad de caracteres, devuelve la cadena resultante después de eliminar 
    las posiciones indicadas utilizando slices
    """
    return cadena[:posicion] + cadena[posicion+cantidad:]


#B

def eliminar_sin_slices(cadena: str, posicion: int, cantidad: int) -> str:
    """recibe una  cadena, una posición y una cantidad de caracteres, devuelve la cadena resultante después de eliminar 
    las posiciones indicadas utilizando un loop.
    """
    resultado = ""
    for i in range(len(cadena)):
        if i < posicion or i >= posicion+cantidad:
            resultado += cadena[i]
    return resultado

def main() -> None:
    """solicita al usuario una cadena, una posición y una cantidad de caracteres, utiliza las funciones
    previas y muestra en pantalla el resultado de las cadenas luego de la eliminación de caracteres.
    """
    cadena = input("Ingrese una cadena: ")
    posicion = int(input("Ingrese la posición de inicio: "))
    cantidad = int(input("Ingrese la cantidad de caracteres: "))
    print("Cadena resultante con slicing:", eliminar_con_slices(cadena, posicion, cantidad))
    print("Cadena resultante sin slicing:", eliminar_sin_slices(cadena, posicion, cantidad))
    
if  __name__ == "__main__":
    main()
