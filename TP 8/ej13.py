#Ej 13

"""Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario.
Comprobar el comportamiento de la función mediante un programa apropiado.
"""

def buscar_clave(diccionario: dict, valor) -> list:
    """
    Busca las claves que mapean al valor dado en el diccionario.
    """
    return [clave for clave, val in diccionario.items() if val == valor]

diccionario = {
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 3
    }

def main() -> None:
    
    valor_a_buscar = 1
    claves = buscar_clave(diccionario, valor_a_buscar)
    print(f"Las claves que corresponden al valor {valor_a_buscar} son: {claves}")

if __name__ == "__main__":
    main()