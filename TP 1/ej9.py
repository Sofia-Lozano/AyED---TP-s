#Ej 9
"""Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación
del camión no debe ser inferior al 80%; en caso contrario el camión no serán despachado por su alto costo.
"""
import random

def peso_naranja() -> int:
    return random.randint(150, 350)

def clasificar_naranja(peso: int) -> str:
    if 200 <= peso <= 300:
        return "cajon"
    else:
        return "jugo"

def llenar_cajones(pesos: list) -> tuple:
    """
    Clasifica las naranjas en cajones o jugo, calcula cuántos cajones completos se llenan,
    cuántas naranjas son para jugo y cuántas naranjas quedan sobrantes.
    """
    naranjas = [p for p in pesos if clasificar_naranja(p) == "cajon"]
    jugo = len(pesos) - len(naranjas)
    cajones_completos = len(naranjas) // 100
    sobrante = len(naranjas) % 100
    return cajones_completos, jugo, sobrante, naranjas

def calcular_camiones(cajones: int, pesos_naranjas: list) -> int:
    """
    Calcula cuántos camiones se necesitan para transportar los cajones llenos,
    considerando que cada camión puede transportar hasta 500 kg y debe estar al menos al 80% lleno.
    """
    naranjas_en_cajones = cajones * 100
    pesos_cajones = pesos_naranjas[:naranjas_en_cajones]
    peso_total_kg = sum(pesos_cajones) / 1000 
    
    capacidad_camion = 500  
    ocupacion_minima = 0.8 * capacidad_camion  
    
    camiones = 0
    peso_restante = peso_total_kg
    
    while peso_restante > 0:
        if peso_restante >= ocupacion_minima:
            camiones += 1
            peso_restante -= capacidad_camion
        else:
            break
    
    return camiones

def main():
    naranjas_cosechadas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    pesos = [peso_naranja() for _ in range(naranjas_cosechadas)]
    
    cajones, jugo, sobrante, naranjas_validas = llenar_cajones(pesos)
    camiones = calcular_camiones(cajones, naranjas_validas)
    
    print(f"Se pueden llenar {cajones} cajones completos.")
    print(f"Se tienen {jugo} naranjas para jugo.")
    print(f"Se tienen {sobrante} naranjas sobrantes para el siguiente reparto.")
    print(f"Se necesitan {camiones} camiones para transportar la cosecha.")

if __name__ == "__main__":
    main()
