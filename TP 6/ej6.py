#Ej 6
"""Un hotel necesita un programa para gestionar la operación de sus habitaciones. El hotel
cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo familiar que se aloja
en el mismo se registra la siguiente información:
· DNI del cliente (número entero)
· Apellido y Nombre
· Fecha de ingreso (DDMMAAAA)
· Fecha de egreso (DDMMAAAA)
· Cantidad de ocupantes
Se solicita desarrollar un programa para realizar las siguientes tareas:
· Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1.
Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos
los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden
repetirse y que la fecha de salida debe ser mayor a la de entrada.
Finalizado el ingreso de huéspedes se solicita:
a. Leer el archivo de huéspedes y asignar la habitaciones a cada uno. El piso y
habitación son asignados arbitrariamente, y no puede asignarse una habitación ya
otorgada.
b. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
c. Mostrar cuántas habitaciones vacías hay en todo el hotel.
d. Mostrar el piso con mayor cantidad de personas.
e. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se ingresa
por teclado. Mostrar todas las que correspondan.
f. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado por
cantidad de días de alojamiento.
"""

import csv
from datetime import datetime
from typing import List, Dict, Any, Tuple

ARCHIVO_HUESPEDES = "huespedes.csv"


def grabar_huespedes() -> None:
    """
    Registra huéspedes hasta que se ingrese DNI = -1.
    Valida duplicados y fechas.
    """
    huespedes: List[Dict[str, Any]] = []
    dnis = set()

    while True:
        dni = int(input("DNI (-1 para finalizar): "))
        if dni == -1:
            break
        if dni in dnis:
            print("DNI repetido. Intente nuevamente.")
            continue

        apellido_nombre = input("Apellido y Nombre: ").strip()
        fecha_ingreso = input("Fecha de ingreso (DDMMAAAA): ").strip()
        fecha_egreso = input("Fecha de egreso (DDMMAAAA): ").strip()
        ocupantes = int(input("Cantidad de ocupantes: "))

        try:
            fi = datetime.strptime(fecha_ingreso, "%d%m%Y")
            fe = datetime.strptime(fecha_egreso, "%d%m%Y")
            if fe <= fi:
                print("La fecha de egreso debe ser posterior a la de ingreso.")
                continue
        except ValueError:
            print("Formato de fecha incorrecto.")
            continue

        huespedes.append({
            "dni": dni,
            "apellido_nombre": apellido_nombre,
            "fecha_ingreso": fecha_ingreso,
            "fecha_egreso": fecha_egreso,
            "ocupantes": ocupantes
        })
        dnis.add(dni)

    if huespedes:
        with open(ARCHIVO_HUESPEDES, "w", newline="", encoding="utf-8") as archivo:
            campos = ["dni", "apellido_nombre", "fecha_ingreso", "fecha_egreso", "ocupantes"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(huespedes)
        print("Datos guardados correctamente.")
    else:
        print("No se registraron huéspedes.")


def leer_huespedes() -> List[Dict[str, Any]]:
    """
    Lee el archivo CSV de huéspedes.
    """
    with open(ARCHIVO_HUESPEDES, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return [dict(fila) for fila in lector]


def asignar_habitaciones(huespedes: List[Dict[str, Any]]) -> Dict[Tuple[int, int], Dict[str, Any]]:
    """
    Asigna habitaciones automáticamente (10 pisos x 6 habitaciones).
    """
    hotel: Dict[Tuple[int, int], Dict[str, Any]] = {}
    piso, habitacion = 1, 1

    for h in huespedes:
        if piso > 10:
            print("Hotel completo. No se pueden asignar más habitaciones.")
            break
        hotel[(piso, habitacion)] = h
        habitacion += 1
        if habitacion > 6:
            habitacion = 1
            piso += 1

    return hotel


def piso_mas_ocupado(hotel: Dict[Tuple[int, int], Dict[str, Any]]) -> int:
    ocupacion = {piso: 0 for piso in range(1, 11)}
    for (piso, _), _ in hotel.items():
        ocupacion[piso] += 1
    return max(ocupacion, key=lambda x: ocupacion[x])


def habitaciones_vacias(hotel: Dict[Tuple[int, int], Dict[str, Any]]) -> int:
    return 10 * 6 - len(hotel)


def piso_con_mas_personas(hotel: Dict[Tuple[int, int], Dict[str, Any]]) -> int:
    personas = {piso: 0 for piso in range(1, 11)}
    for (piso, _), datos in hotel.items():
        personas[piso] += int(datos["ocupantes"])
    return max(personas, key=lambda p: personas[p])


def proximas_habitaciones_desocupadas(hotel: Dict[Tuple[int, int], Dict[str, Any]]) -> List[Tuple[int, int]]:
    fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ").strip()
    try:
        fa = datetime.strptime(fecha_actual, "%d%m%Y")
    except ValueError:
        print("Formato de fecha incorrecto.")
        return []

    proximas: List[Tuple[int, int]] = []
    menor_fecha = None

    for hab, datos in hotel.items():
        fe = datetime.strptime(datos["fecha_egreso"], "%d%m%Y")
        if fe >= fa:
            if menor_fecha is None or fe < menor_fecha:
                menor_fecha = fe
                proximas = [hab]
            elif fe == menor_fecha:
                proximas.append(hab)

    return proximas


def listado_por_dias(hotel: Dict[Tuple[int, int], Dict[str, Any]]) -> List[Dict[str, Any]]:
    lista = []
    for (piso, hab), datos in hotel.items():
        fi = datetime.strptime(datos["fecha_ingreso"], "%d%m%Y")
        fe = datetime.strptime(datos["fecha_egreso"], "%d%m%Y")
        dias = (fe - fi).days
        lista.append({
            "dni": datos["dni"],
            "apellido_nombre": datos["apellido_nombre"],
            "dias": dias,
            "habitacion": f"Piso {piso} - Hab {hab}"
        })
    return sorted(lista, key=lambda x: x["dias"], reverse=True)


def main() -> None:
    print("=== GESTIÓN DE HOTEL ===")
    grabar_huespedes()
    huespedes = leer_huespedes()
    hotel = asignar_habitaciones(huespedes)

    print(f"\nPiso más ocupado: {piso_mas_ocupado(hotel)}")
    print(f"Habitaciones vacías: {habitaciones_vacias(hotel)}")
    print(f"Piso con más personas: {piso_con_mas_personas(hotel)}")

    prox = proximas_habitaciones_desocupadas(hotel)
    if prox:
        print("Próximas habitaciones en desocuparse:")
        for p, h in prox:
            print(f" - Piso {p}, Habitación {h}")
    else:
        print("No hay habitaciones próximas a desocuparse.")

    print("\nListado de huéspedes por días de alojamiento:")
    for item in listado_por_dias(hotel):
        print(f"{item['apellido_nombre']} - {item['dias']} días - {item['habitacion']}")


if __name__ == "__main__":
    main()
