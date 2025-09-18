#Ej 1
"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe.
"""
def mayor (a: int, b: int, c: int) -> int:
    """
    recibe tres números enteros y los compara para determinar si son distintos entre sí.
    si existen dos números iguales, devuelve -1, si los tres números son distintos, los compara para determinar el mayor
    """
    if a == b:
        if a == c:
            return -1
        else:
            return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

def main() -> None:
    """
    Solicita al usuario tres números enteros, utiliza la función mayor y en caso de hallar 
    un mayor estricto, devuelve el número. Caso contrario, informa que no se hallo un mayor estricto.
    """
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))

    maximo = mayor(a, b, c)

    if maximo == -1:
        print("No hay un mayor estricto.")
    else:
        print(f"El mayor estricto es: {maximo}")

if __name__ == "__main__":
    main()