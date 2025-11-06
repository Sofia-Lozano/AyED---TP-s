#Ej 2
"""Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse
después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""

def dividir_archivo(nombre_archivo: str, tam_max: int) -> None:
    """
    Divide un archivo de texto en partes cuyo tamaño máximo (en bytes) se ingresa por teclado.
    Los archivos generados mantienen el nombre original con un sufijo indicando la parte.
    No carga el archivo completo en memoria.
    """
    try:
        if tam_max <= 0:
            raise ValueError("El tamaño máximo debe ser mayor que cero.")

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            parte = 1
            while True:
                datos = archivo.read(tam_max)
                if not datos:
                    break
                nuevo_nombre = f"{nombre_archivo}_parte{parte}.txt"
                with open(nuevo_nombre, "w", encoding="utf-8") as salida:
                    salida.write(datos)
                print(f"Generado: {nuevo_nombre}")
                parte += 1

        print("División completada exitosamente.")
    except FileNotFoundError:
        print("Error: el archivo especificado no existe.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    try:
        archivo = input("Ingrese el nombre del archivo a dividir: ").strip()
        tam = int(input("Ingrese el tamaño máximo por parte (en bytes): "))
        dividir_archivo(archivo, tam)
    except ValueError:
        print("Error: debe ingresar un número válido para el tamaño.")