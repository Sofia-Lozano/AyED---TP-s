#Ej 3
"""Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro
de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo)
se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva
el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.
"""
def calcular_gasto(viajes: int) -> float:
    """
    calcula el costo total de las tarifas en base a los descuentos por cantidad de viajes.
    """
    if viajes < 1:
        return 0.0
    gasto = 0.0
    if viajes <= 20:
        gasto = viajes * 2.5
    elif viajes <= 40:
        gasto = 20 * 2.5 + (viajes - 20) * 2.0
    elif viajes <= 60:
        gasto = 20 * 2.5 + 20 * 2.0 + (viajes - 40) * 1.5
    else:
        gasto = 20 * 2.5 + 20 * 2.0 + 20 * 1.5 + (viajes - 60) * 1.0
    return gasto

def main() -> None:
    """
    solicita al usuario la cantidad de viajes realizados o a realizar, utiliza la función calcular_gasto
    e informa al usuario del gasto total.
    """
    viajes = int(input("Ingrese el número de viajes: "))
    gasto_total = calcular_gasto(viajes)
    print(f"El gasto total es: ${gasto_total:.2f}")

if __name__ == "__main__":
    main()