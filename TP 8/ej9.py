#Ej 9

"""Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""

def main() -> None:
    n = int(input("Ingrese un número entero: "))
    tabla = {i: n * i for i in range(1, 13)}
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 13):
        print(f"{n} x {i} = {tabla[i]}")

if __name__ == "__main__":
    main()