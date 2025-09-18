#Ej 8
"""la siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para 
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
y año cualquiera basándose en la función suministrada. Considerar que la semana comienza en domingo.
"""
def diadelasemana(dia,mes,anio):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
        siglo = anio // 100
        anio2 = anio % 100
    dia_sem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if dia_sem < 0:
        dia_sem = dia_sem + 7
    return dia_sem

def imprimir_calendario(mes: int, año: int) -> None:
    """
    imprime  el calendario de un mes completo, brindando formato y teniendo
    en cuenta los años  bisiestos.
    """
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        dias_mes[2] = 29
    dia_inicio = diadelasemana(1, mes, año)
    print("Sun  Mon  Tue  Wed  Thu  Fri  Sat")
    print("----------------------------------")
    for _ in range(dia_inicio):
        print("    ", end="")
    for dia in range(1, dias_mes[mes] + 1):
        print(f"{dia:4}", end="")
        if (dia_inicio + dia - 1) % 7 == 6:
            print()
    print()
    
imprimir_calendario(9,2025)