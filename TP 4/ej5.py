#Ej 5
"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva
otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filte
"""
#A

def filtrar_palabras_loop(frase: str, n: int) -> str:
    """recibe dos parámetros, un string y un entero.
    filtra las palabras que tengan la cantidad de caracteres especificada, utilizando
    ciclos normales.
    devuelve  una string con las palabras filtradas
    """
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
    return ' '.join(resultado)
#B

def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """recibe dos parámetros, un string y un entero.
    filtra las palabras que tengan la cantidad de caracteres especificada, utilizando
    una lista por comprensión.
    devuelve  una string con las palabras filtradas
    """
    palabras = frase.split()
    return ' '.join([palabra for palabra in palabras if len(palabra) >= n])


#C

def filtrar_palabras_filter(frase: str, n: int) -> str:
    """recibe dos parámetros, un string y un entero.
    filtra las palabras que tengan la cantidad de caracteres especificada, utilizando
    una la función de orden superior filter .
    devuelve  una string con las palabras filtradas
    """
    palabras = frase.split()
    return ' '.join(list(filter(lambda palabra: len(palabra) >= n, palabras)))

def main() -> None:
    """solicita al usuario una frase y un entero para utilizar como parámetro a filtrar en 
    las opciones, muestra los resultados de las frases filtradas en pantalla
    """
    frase = input("Ingrese una frase: ")
    n = int(input("Ingrese el número de caracteres mínimos: "))
    print("Filtrado con ciclo normal:", filtrar_palabras_loop(frase, n))
    print("Filtrado con lista por comprensión:", filtrar_palabras_comprension(frase, n))
    print("Filtrado con función filter:", filtrar_palabras_filter(frase, n))
    
if  __name__ == "__main__":
    main()
