#Ej 3
"""Los números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
"""
    
def extraer_claves(clave_maestra: int) -> tuple:
    """recibe como parámetro una clave maestra, la transforma a string y la divide
    extrayendo dos llaves de la misma, retorna una tupla.
    """
    clave_maestra_str = str(clave_maestra)
    clave1 = "".join([clave_maestra_str[i] for i in range(0, len(clave_maestra_str), 2)])
    clave2 = "".join([clave_maestra_str[i] for i in range(1, len(clave_maestra_str), 2)])
    return int(clave1), int(clave2)

def main() -> None:
    """solicita al usuario la clave maestra y emplea la función extraer_claves, devuelve
    las claves separadas.
    """
    clave_maestra = int(input("Ingrese la clave maestra: "))
    clave1, clave2 = extraer_claves(clave_maestra)
    print("Clave 1:", clave1)
    print("Clave 2:", clave2)
    
if  __name__ == "__main__":
    main()
