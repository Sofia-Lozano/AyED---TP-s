#Ej 12

"""Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""
def crear_lista_precios() -> dict[str, float]:
    """
    Crea un diccionario con los productos y sus precios ingresados por el usuario.
    Finaliza cuando se ingresa un nombre vacío.
    """
    lista_precios = {}
    while True:
        producto = input("Ingrese el nombre del producto (Enter para finalizar): ").strip()
        if not producto:
            break
        try:
            precio = float(input(f"Ingrese el precio de '{producto}': "))
            lista_precios[producto.lower()] = precio
        except ValueError:
            print("Error: el precio debe ser un número válido.")
    return lista_precios


def incrementar_precios_cuadernos(lista_precios: dict[str, float]) -> None:
    """
    Incrementa en un 15% el precio de los cuadernos (productos que contengan 'cuaderno' en su nombre).
    """
    for producto in lista_precios:
        if "cuaderno" in producto:
            lista_precios[producto] *= 1.15


def mostrar_listado(lista_precios: dict[str, float]) -> None:
    """
    Muestra el listado de productos y sus precios.
    """
    print("\nListado de precios actualizados:")
    for producto, precio in lista_precios.items():
        print(f"{producto.title():<20} ${precio:>8.2f}")


def obtener_item_mas_costoso(lista_precios: dict[str, float]) -> tuple[str, float]:
    """
    Devuelve una tupla con el nombre y el precio del ítem más costoso.
    """
    return max(lista_precios.items(), key=lambda x: x[1])


def main() -> None:
    lista_precios = crear_lista_precios()

    if not lista_precios:
        print("No se ingresaron productos.")
        return

    incrementar_precios_cuadernos(lista_precios)
    mostrar_listado(lista_precios)

    item, precio = obtener_item_mas_costoso(lista_precios)
    print(f"\nEl ítem más costoso es '{item.title()}' con un precio de ${precio:.2f}.")


if __name__ == "__main__":
    main()
