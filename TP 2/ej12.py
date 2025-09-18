#Ej 12
"""Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron
"""
#A
def procesar_entradas() -> dict:
    """solicitamos al usuario el número de socio y se agrega la entrada correspondiente en el diccionario.
    """
    entradas = {}
    while True:
        num_socio = int(input("Ingrese el número de socio, 0 para finalizar: "))
        if num_socio == 0:
            break
        if num_socio in entradas:
            entradas[num_socio] += 1
        else:
            entradas[num_socio] = 1
    return entradas

#B
def eliminar_socio(entradas: dict, num_socio: int) -> int:
    """tomando el número de socio, se busca la coincidencia en el diccionario y si se encuentra,
    se eliminan todas las entradas correspondientes. caso contrario se informa al usuario de  que el socio no existe.

    """
    if num_socio in entradas:
        num_entradas = entradas[num_socio]
        del entradas[num_socio]
        return num_entradas
    else:
        return ('El número de socio ingresado no existe')
    
def main() -> None:
    """utilizando las funciones anteriores mostramos por pantalla los registros completos de entradas. se pide al usuario el número de socio
    a dar de baja, confirmamos la baja y mostramos la lista actualizada luego de dar de baja al socio.
    """
    entradas = procesar_entradas()
    print("Registros de entrada al club:")
    for num_socio, num_entradas in entradas.items():
        print(f"Socio {num_socio}: {num_entradas} entradas")
    
    num_socio_baja = int(input("Ingrese el número de socio que se dio de baja: "))
    print("Registros de entrada al club antes de eliminar:")
    for num_socio, num_entradas in entradas.items():
        print(f"Socio {num_socio}: {num_entradas} entradas")
    
    num_entradas_eliminadas = eliminar_socio(entradas, num_socio_baja)
    print(f"Se eliminaron {num_entradas_eliminadas} entradas del socio {num_socio_baja}")
    
    print("Registros de entrada al club después de eliminar:")
    for num_socio, num_entradas in entradas.items():
        print(f"Socio {num_socio}: {num_entradas} entradas")
        
if  __name__ == "__main__":
    main()

