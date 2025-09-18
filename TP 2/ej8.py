#Ej 8
"""Utilizar la técnica de listas por comprensión para construir una lista con todos los 
números impares comprendidos entre 100 y 200.
"""
def generar_impares() -> list:
    """generamos y retornamos una lista por comprensión que contiene los números impares entre  100 y 200
    """
    return [num for num in range(100, 201) if num % 2 != 0]

def main() -> None:
    lista_impares = generar_impares()
    print("Lista de números impares entre 100 y 200:", lista_impares)
    
if  __name__ == "__main__":
    main()
