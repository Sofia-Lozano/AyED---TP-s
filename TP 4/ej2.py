#Ej 2
"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la 
misma tiene 80 columnas.
"""
def centrar_cadena(cadena: str) -> str:
    """recibe una cadena como parámetro y la retorna centrada en pantalla
    """
    ancho_pantalla = 80
    longitud_cadena = len(cadena)
    espacios_izquierda = (ancho_pantalla - longitud_cadena) // 2
    espacios_derecha = ancho_pantalla - longitud_cadena - espacios_izquierda
    return " " * espacios_izquierda + cadena + " " * espacios_derecha

def main() -> None:
    """
    solicita al usuario una cadena de caracteres y la muestra centrada en pantalla
    """
    cadena = input("Ingrese una cadena de caracteres: ")
    cadena_centrada = centrar_cadena(cadena)
    print(cadena_centrada)
    
if  __name__ == "__main__":
    main()
