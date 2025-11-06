#Ej 10
""". Desarrollar una función para reemplazar todas las apariciones de una palabra por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
palabras completas, y no fragmentos de palabras. Escribir también un programa 
para verificar el comportamiento de la función.
"""

def reemplazar_palabra(cadena: str, palabra_a_reemplazar: str, nueva_palabra: str) -> tuple[str, int]:
    """recibe como parámetro una lista de palabras, una palabra a reemplazar y una nueva palabra que ocupe su lugar.
    devuelve una lista con la palabra reemplazada y la cantidad de veces que ha sido reemplazada.
    """
    palabras = cadena.split()
    reemplazos = 0
    nueva_cadena = []
    for palabra in palabras:
        if palabra.lower() == palabra_a_reemplazar.lower():
            nueva_cadena.append(nueva_palabra)
            reemplazos += 1
        else:
            nueva_cadena.append(palabra)
    resultado = ' '.join(nueva_cadena)
    
    return resultado, reemplazos


cadena = "Esta es una cadena de prueba."
palabra_a_reemplazar = "cadena"
nueva_palabra = "string"

resultado, reemplazos = reemplazar_palabra(cadena, palabra_a_reemplazar, nueva_palabra)

print("Cadena original:", cadena)
print("Nueva cadena:", resultado)
print("Cantidad de palabras reemplazadas:", reemplazos)