#Ej 11
"""1. Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como número de afiliado. 
"""
#A
def procesar_pacientes() -> dict:
    """solicitamos al usuario los datos del paciente y clasificamos los pacientes por el tipo
    de atención requerida. guardamos los datos en un diccionario.
    """
    pacientes = {"urgencia": [], "turno": []}
    while True:
        num_afiliado = int(input("Ingrese el número de afiliado, -1 para finalizar: "))
        if num_afiliado == -1:
            break
        tipo_atencion = int(input("Ingrese 0 para urgencia, 1 para turno: "))
        if tipo_atencion == 0:
            pacientes["urgencia"].append(num_afiliado)
        elif tipo_atencion == 1:
            pacientes["turno"].append(num_afiliado)
    return pacientes

#B
def buscar_paciente(pacientes: dict) -> None:
    """solicitamos al usuario el número de afiliado del paciente y buscamos en el registro la
    cantidad de veces que ha sido atendido por turno y por urgencia.
    """
    while True:
        num_afiliado = int(input("Ingrese el número de afiliado a buscar, -1 para finalizar: "))
        if num_afiliado == -1:
            break
        conteo_urgencias = pacientes["urgencia"].count(num_afiliado)
        conteo_turnos = pacientes["turno"].count(num_afiliado)
        print(f"El paciente {num_afiliado} fue atendido por urgencia {conteo_urgencias} veces y por turno {conteo_turnos} veces.")
        
def main() -> None:
    """
    invocamos las funciones previas y mostramos el resultado en pantalla 
    """
    pacientes = procesar_pacientes()
    print("Pacientes atendidos por urgencia:", pacientes["urgencia"])
    print("Pacientes atendidos por turno:", pacientes["turno"])
    buscar_paciente(pacientes)
    
if __name__ == "__main__":
    main()