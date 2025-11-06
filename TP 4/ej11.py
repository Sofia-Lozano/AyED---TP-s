#Ej 11
"""Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro 
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los 
caracteres de la subcadena no necesariamente deben estar en forma consecutiva 
dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
Cadena:
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva 
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Sub-cadena: UADE
Cantidad encontrada: 4 (Las coincidencias están resaltadas en la cadena siguiente)
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva 
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
"""

def contar_subsecuencia(cadena: str, subcadena: str) -> int:
    """recibe como parámetro una cadena principal y una subcadena que contien los elementos a buscar,
     y cuenta las ocurrencias de la subcadena, ignorando mayúsculas, minúsculas y caracteres no consecutivos.
    """
    cadena_minúscula = cadena.lower()
    subcadena_minúscula = subcadena.lower()
    ocurrencias = 0
    índice = 0
    while índice < len(cadena_minúscula):
        coincidencia = True
        sub_índice = 0
        while sub_índice < len(subcadena_minúscula):
            índice = cadena_minúscula.find(subcadena_minúscula[sub_índice], índice)
            if índice == -1:
                coincidencia = False
                break
            índice += 1
            sub_índice += 1
        if coincidencia:
            ocurrencias += 1
        índice = índice - sub_índice + 1
    return ocurrencias


cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos.Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
subcadena = "UADE"

ocurrencias = contar_subsecuencia(cadena, subcadena)

print("Cadena:", cadena)
print("Sub-cadena:", subcadena)
print("Cantidad encontrada:", ocurrencias)