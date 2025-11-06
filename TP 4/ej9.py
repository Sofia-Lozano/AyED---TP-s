#Ej 9
"""Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las palabras se encuentran separadas por uno o más espacios. Devolver otra 
cadena con las palabras ordenadas según su longitud, dejando un espacio entre 
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la 
longitud de las palabras, pero deberán conservarse en la cadena final
"""

import re

def ordenar_palabras_por_largo(cadena: str) -> str:
    """recibe como parámetro  una cadena de caracteres y devuelve otra cadena con las palabras ordenadas según su longitud,
    no cuenta los signos de puntuación como palabras pero los mantiene en la cadena final
    """
    palabras = re.findall(r'\b\w[\w\'\-]*\b|[^\w\s]', cadena)
    palabras_ordenadas = sorted(palabras, key=lambda x: len(re.sub(r'[^\w]', '', x)))
    resultado = ' '.join(palabras_ordenadas)
    return resultado


print(ordenar_palabras_por_largo ('Esta cadena va a estar ordenada por el largo de sus palabras.'))