#Ej 7
"""Intercalar los elementos de una lista entre los elementos de otra. La intercalación 
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
tener distintas longitudes
"""

def intercalar(lista1: list, lista2: list) -> None:
    """recibimos dos listas como parámetros e intercalamos sus elementos uno
    por uno utilizando slices.
    """
    i = 0
    for elem in lista2:
        lista1[i:i] = [elem]
        i += 2
        
def main() -> None:
    """
    utilizando la función previa, intercalamos los elementos de lista1 y lista2.
    mostramos las listas originales y la intercalada.
    """
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7, 2, 5]
    
    print("Lista 1 original:", lista1)
    print("Lista 2:", lista2)
    intercalar(lista1, lista2)
    print("Lista 1 modificada:", lista1)
    
if  __name__ == "__main__":
    main()
