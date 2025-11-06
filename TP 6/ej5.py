#Ej 5

"""Se dispone de dos formatos diferentes de archivos de texto en los que se almacenan
datos de empleados, detallados más abajo. Desarrollar un programa para convertir
cada uno de los formatos suministrados, grabando los datos obtenidos en
otro archivo con formato CSV. Los archivos de entrada pueden generarse con Block
de Notas o cualquier otro editor, copiando y pegando los ejemplos proporcionados.
Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta
y Domicilio.
Formato 1: Los campos tienen longitud fija con un espacio de separación
entre ellos.
(Regla) 1 2 3 4 5 6
012345678901234567890123456789012345678901234567890123456789012
Pérez Juan 20080211 Corrientes 348
González Ana M 20080115 Juan de Garay 1111 3er piso dto A
Formato 2: Todos los campos de este archivo están precedidos por un
número de dos dígitos que indica la longitud del campo que sigue.
10Pérez Juan082008021114Corrientes 348
14González Ana M082008011533Juan de Garay 1111 3er piso dto A
NOTAS:
· Los espacios que se encuentren al final de las cadenas en el formato 1 deberán
ser eliminados.
· El formato 2 debe generalizarse para que soporte registros con cualquier cantidad
de campos.
"""

import csv

def convertir_formato_1(nombre_entrada: str, nombre_salida: str) -> None:
    """
    Convierte un archivo de texto con formato fijo (Formato 1)
    en un archivo CSV con los campos:
    Apellido y Nombre, Fecha de Alta, Domicilio.
    """
    try:
        with open(nombre_entrada, "r", encoding="utf-8") as entrada, \
             open(nombre_salida, "w", newline="", encoding="utf-8") as salida:
            escritor = csv.writer(salida)
            escritor.writerow(["Apellido y Nombre", "Fecha de Alta", "Domicilio"])

            for linea in entrada:
                linea = linea.rstrip()
                if not linea:
                    continue

                apellido_nombre = linea[0:20].strip()
                fecha_alta = linea[20:28].strip()
                domicilio = linea[29:].strip()
                escritor.writerow([apellido_nombre, fecha_alta, domicilio])

        print(f"Conversión de formato 1 completada: {nombre_salida}")

    except FileNotFoundError:
        print("Error: el archivo especificado no existe.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


def convertir_formato_2(nombre_entrada: str, nombre_salida: str) -> None:
    """
    Convierte un archivo de texto en formato 2 (campos precedidos por longitud de 2 dígitos)
    en un archivo CSV. Soporta cualquier cantidad de campos por registro.
    """
    try:
        with open(nombre_entrada, "r", encoding="utf-8") as entrada, \
             open(nombre_salida, "w", newline="", encoding="utf-8") as salida:
            escritor = csv.writer(salida)
            escritor.writerow(["Campo 1", "Campo 2", "Campo 3", "..."])

            for linea in entrada:
                linea = linea.strip()
                if not linea:
                    continue

                i = 0
                campos = []
                while i < len(linea):
                    if i + 2 > len(linea):
                        break
                    try:
                        longitud = int(linea[i:i + 2])
                    except ValueError:
                        break
                    i += 2
                    campo = linea[i:i + longitud]
                    campos.append(campo)
                    i += longitud
                escritor.writerow(campos)

        print(f"Conversión de formato 2 completada: {nombre_salida}")

    except FileNotFoundError:
        print("Error: el archivo especificado no existe.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


if __name__ == "__main__":
    print("=== Conversor de archivos de empleados a CSV ===")
    print("1. Formato 1 (campos de longitud fija)")
    print("2. Formato 2 (campos con longitud variable)")
    opcion = input("Seleccione el formato (1 o 2): ").strip()

    archivo_entrada = input("Ingrese el nombre del archivo de entrada: ").strip()
    archivo_salida = input("Ingrese el nombre del archivo CSV de salida: ").strip()

    if opcion == "1":
        convertir_formato_1(archivo_entrada, archivo_salida)
    elif opcion == "2":
        convertir_formato_2(archivo_entrada, archivo_salida)
    else:
        print("Opción no válida.")
