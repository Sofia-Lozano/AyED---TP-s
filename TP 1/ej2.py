#Ej 2
"""
Desarrollar una función que reciba tres números enteros positivos correspondientes 
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
Devolver True o False según la fecha sea correcta o no. Realizar también un 
programa para verificar el comportamiento de la función.
"""
def es_fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    verifica si la fecha ingresada es válida, tomando como referencia la cantidad de meses y el número
    de días en cada mes. También toma en cuenta los años bisisestos.
    """
    if mes < 1 or mes > 12:
        return False

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia < 1 or dia > 31:
            return False
    elif mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    else:
        if dia < 1 or dia > 30:
            return False

    return True

def main() -> None:
    """
    solicita al usuario los valores de día, mes y año y los verifica utilizando la función es_fecha_valida.
    informa al usuario la validez o invalidez de la fecha.
    """
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    if es_fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")

if __name__ == "__main__":
    main()