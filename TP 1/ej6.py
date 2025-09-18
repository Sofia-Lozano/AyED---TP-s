#EJ6
"""Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite
utilizar facilidades de Python no vistas en clase.
"""


def concatenar(num1: int, num2: int) -> int:
    str1 = str(num1)
    str2 = str(num2)
    parte1 = str1[:]
    parte2 = str2[:]
    resultado = int(parte1 + parte2)
    return resultado

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))

print(concatenar(num1, num2))  