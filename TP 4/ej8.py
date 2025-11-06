#Ej 8
"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros
"""
    
def obtener_ultimos_caracteres(cadena: str, n: int) -> str:
    """recibe una cadena y un entero, devuelve la cantidad indicada de los últimos caracteres
    de la cadena utilizando slices
    """
    return cadena[-n:]