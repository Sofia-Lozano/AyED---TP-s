#Ej 6
"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres, indicando
la posición y la cantidad de caracteres deseada. Devolver la subcadena como valor de retorno.
Escribir también un programa para verificar el comportamiento de la misma.
Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

#A
def extraer_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """recibe como paraámetros una cadena, un entero  que indica la posición y otro entero que indica la cantidad de caracteres
    a sustraer. devuelve la cadena sustraída utilizando slices.
    """
    return cadena[posicion:posicion+cantidad]

#B
def extraer_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """recibe como parámetros una cadena, un entero  que indica la posición y otro entero que indica la cantidad de caracteres
    a sustraer. devuelve la cadena sustraída utilizando un loop.
    """
    resultado = ""
    for i in range(posicion, posicion+cantidad):
        resultado += cadena[i]
    return resultado

def main() -> None:
    """solicita al usuario  una cadena, una posición y una cantidad de caracteres, utiliza las funciones
    previas y muestra el resultado de las cadenas filtradas en pantalla.
    """
    cadena = input("Ingrese una cadena: ")
    posicion = int(input("Ingrese la posición de inicio: "))
    cantidad = int(input("Ingrese la cantidad de caracteres: "))
    print("Subcadena extraída con slicing:", extraer_rebanadas(cadena, posicion, cantidad))
    print("Subcadena extraída sin slicing:", extraer_sin_rebanadas(cadena, posicion, cantidad))
    

if __name__ ==  "__main__":
    main()
