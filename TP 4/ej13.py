#Ej 13
"""Muchas aplicaciones financieras requieren que los números sean expresados también en letras.
Por ejemplo, el número 2153 puede escribirse como "dos mil ciento cincuenta y tres".
Escribir un programa que utilice una función para convertir un 
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría 
la función si también aceptara números negativos? ¿Y números con decimales?
"""

def numero_a_letras(numero):
    """Convierte un número entero entre 0 y 1 billón a letras.
    """
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"][numero - 10]
    elif numero < 100:
        return decenas[numero // 10] + (" " + unidades[numero % 10] if numero % 10 != 0 else "")
    elif numero < 1000:
        return centenas[numero // 100] + (" " + numero_a_letras(numero % 100) if numero % 100 != 0 else "")
    elif numero < 1000000:
        return numero_a_letras(numero // 1000) + " mil" + (" " + numero_a_letras(numero % 1000) if numero % 1000 != 0 else "")
    elif numero < 1000000000:
        return numero_a_letras(numero // 1000000) + " millones" + (" " + numero_a_letras(numero % 1000000) if numero % 1000000 != 0 else "")
    else:
        return numero_a_letras(numero // 1000000000) + " billones" + (" " + numero_a_letras(numero % 1000000000) if numero % 1000000000 != 0 else "")


numero = 2153
print(f"El número {numero} se escribe como: {numero_a_letras(numero)}")