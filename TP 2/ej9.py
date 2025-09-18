#Ej 9
"""Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""

def generar_multiplos() -> list:
    """solicitamos al usuario dos valores y creamos una lista con todos los números múltiplos de 7 que no son múltiplos
    de 5 comprendidos entre ambos extremos. tomamos en cuenta el rango de números negativos. 
    """
    A = int(input("Ingrese el valor de A: "))
    B = int(input("Ingrese el valor de B: "))
    if  A > B:
        return [num for num in range(B, A+1) if num % 7 == 0 and num % 5 != 0]
    else:
        return [num for num in range(A, B+1) if num % 7 == 0 and num % 5 != 0]

def main() -> None:
    lista_multiplos = generar_multiplos()
    print("Lista de múltiplos de 7 que no son múltiplos de 5:", lista_multiplos)
    
if  __name__ == "__main__":
    main()