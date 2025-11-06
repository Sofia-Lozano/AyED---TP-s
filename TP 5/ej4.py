#Ej 4
"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""

def contar() -> None:
    """
    Imprime los números enteros del 1 al 100000.
    Solicita confirmación antes de detenerse si el usuario presiona Ctrl-C.
    """
    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        respuesta = input("\n¿Desea detener el programa? (s/n): ").strip().lower()
        if respuesta == "s":
            print("Programa detenido por el usuario.")
        else:
            contar()


if __name__ == "__main__":
    contar()
