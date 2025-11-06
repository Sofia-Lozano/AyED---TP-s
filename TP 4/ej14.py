#Ej 14
"""Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que 
una dirección sea considerada válida el nombre de usuario debe poseer solamente 
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe 
tener al menos un carácter y tiene que finalizar con .com o .com.ar. 
Repetir el proceso de validación hasta ingresar una cadena vacía.
Al finalizar mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente, 
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
"""

import re

def validar_direccion(direccion):
    """Verifica si la dirección de correo electrónico proporcionada es válida.
    """
    patron = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$"
    if re.match(patron, direccion):
        return True
    return False

def obtener_dominio(direccion):
    """Obtiene el dominio de la dirección de correo electrónico proporcionada.
    """
    return direccion.split("@")[1]

def main():
    direcciones = []
    dominios = set()
    while True:
        direccion = input("Ingrese una dirección de correo electrónico (o presione Enter para salir): ")
        if not direccion:
            break
        if validar_direccion(direccion):
            direcciones.append(direccion)
            dominios.add(obtener_dominio(direccion).lower())
        else:
            print("Dirección no válida")
    print("Direcciones válidas:")
    for direccion in direcciones:
        print(direccion)
    print("Dominios únicos (ordenados alfabéticamente):")
    for dominio in sorted(dominios):
        print(dominio)

if __name__ == "__main__":
    main()