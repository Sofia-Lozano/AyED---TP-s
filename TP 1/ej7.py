#Ej 7
"""Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera
"""
def diasiguiente(dia: int, mes: int, anio: int) -> tuple:
    """
    Calcula la fecha siguiente a la proporcionada, consultando los días disponibles en cada mes y
    teniendo en cuenta los años bisiestos
    """
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        dias_mes[2] = 29
    if dia < dias_mes[mes]:
        return dia + 1, mes, anio
    elif mes < 12:
        return 1, mes + 1, anio
    else:
        return 1, 1, anio + 1
    
#A
def sumar_dias(dia: int, mes: int, anio: int, n: int) -> tuple:
    """
    utilizando la función diasiguiente y el parámetro n recibido, cuenta los días desde la fecha ingresada hasta fecha + n,
    devuelve la nueva fecha
    """
    for _ in range(n):
        dia, mes, anio = diasiguiente(dia, mes, anio)
    return dia, mes, anio

#B
def dias_entre_fechas(dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int) -> int:
    """
    recibe dos conjuntos de parámetros (día,mes,año). En caso de que no sean la misma fecha, utiliza la función
    diasiguiente y un contador para calcular la diferencia de días entre ambas fechas.
    """
    dias = 0
    while (dia1, mes1, anio1) != (dia2, mes2, anio2):
        dia1, mes1, anio1 = diasiguiente(dia1, mes1, anio1)
        dias += 1
    return dias