#Ej 11

"""Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""
def contar_vocales(palabra: str) -> dict:
    """
    Cuenta la cantidad de vocales en una palabra.
    devuelve un diccionario con la cantidad de vocales halladas.
    """
    vocales = "aeiou"
    contador = {vocal: 0 for vocal in vocales}
    for letra in palabra.lower():
        if letra in contador:
            contador[letra] += 1
    return contador

def main() -> None:
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    for palabra in palabras:
        resultado = contar_vocales(palabra)
        print(f"Palabra: {palabra}, Vocales: {resultado}")

if __name__ == "__main__":
    main()