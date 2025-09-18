#Ej 3
"""Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 
"""
def generar_cuadrados() -> list:
    """solicitamos al usuario el valor de n y creamos una lista los elemntos al cuadrado entre 1 y n
    """
    n = int(input("Ingrese un número entero: "))
    lista_cuadrados = [i ** 2 for i in range(1, n + 1)]
    return lista_cuadrados

def main() -> None:
    """utilizando la funcion generar_cuadrados, creamos una lista e imprimimos los ultimos 10 valores 
    de esta
    """
    lista_cuadrados = generar_cuadrados()
    print("Lista de cuadrados:", lista_cuadrados)
    
    ultimos_10_valores = lista_cuadrados[-10:] 
    print("Últimos 10 valores de la lista:", ultimos_10_valores)
    
if  __name__ == "__main__":
    main()
