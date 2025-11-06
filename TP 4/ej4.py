#Ej 4
"""Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En 
qué cambiaría la función si el rango de valores fuese diferente?
"""
def entero_a_romano(num: int) -> str:
    """recibimos un entero como parámetro y lo transformamos en su equivalente romano 
    utilizando listas
    """
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]
    simbolos = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    num_romano = ''
    i = 0
    while  num > 0:
        for _ in range(num // valores[i]):
            num_romano += simbolos[i]
            num -= valores[i]
        i += 1
    return num_romano

def main() -> None:
    """solicita al usuario un número entero, verifica que se encuentre en el rango
    de 0 a 3999 y lo convierte a romano utilizando la
    función entero_a_romano. Muestra los resultados en pantalla.
    """
    num = int(input("Ingrese un número entre 0 y 3999: "))
    if not 0 <= num <= 3999:
        print("El número debe estar entre 0 y 3999")
    else:
        num_romano = entero_a_romano(num)
        print("El número romano es:", num_romano)
        
if  __name__ == "__main__":
    main()
