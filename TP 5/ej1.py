#Ej 1
"""Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento
de la misma.
"""

def ingresar_numero_natural() -> int:
    """
    Solicita al usuario ingresar un número natural (> 0).
    Valida el ingreso con manejo de excepciones y muestra mensajes de error específicos.
    Devuelve el número cuando es válido.
    """
    while True:
        try:
            valor = input("Ingrese un número natural: ").strip()
            if valor == "":
                raise ValueError("No ingresó ningún valor.")
            numero = float(valor)
            if not numero.is_integer():
                raise ValueError("El número ingresado no es un entero.")
            numero = int(numero)
            if numero <= 0:
                raise ValueError("El número debe ser mayor que cero.")
            return numero
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    print("Prueba de ingreso de número natural")
    print("=" * 40)
    n = ingresar_numero_natural()
    print(f"✅ Número ingresado correctamente: {n}")
