#Ej 10

"""Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

def eliminar_claves(diccionario: dict, claves: list) -> tuple:
    """
    Elimina las claves especificadas de un diccionario.
    devuelve el diccionario modificado y la cantidad de claves eliminadas.
    """
    cantidad_eliminadas = 0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            cantidad_eliminadas += 1
    return diccionario, cantidad_eliminadas

def main() -> None:
    diccionario = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"}
    claves_a_eliminar = [2, 4]

    print("Diccionario original:")
    print(diccionario)

    diccionario_modificado, cantidad = eliminar_claves(diccionario, claves_a_eliminar)

    print("\nDiccionario modificado:")
    print(diccionario_modificado)
    print(f"Cantidad de claves eliminadas: {cantidad}")

if __name__ == "__main__":
    main()