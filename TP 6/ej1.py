#Ej 1
"""Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos
y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena
"IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
"""

def clasificar_apellidos(nombre_archivo: str) -> None:
    """
    Lee un archivo de texto con nombres en formato 'Apellido, Nombre'
    y guarda en archivos separados según el sufijo del apellido
    Descarta el resto.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        armenia, italia, espania = [], [], []

        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue
            apellido = linea.split(",")[0].strip().upper()
            if apellido.endswith("IAN"):
                armenia.append(linea)
            elif apellido.endswith("INI"):
                italia.append(linea)
            elif apellido.endswith("EZ"):
                espania.append(linea)

        if armenia:
            with open("ARMENIA.TXT", "w", encoding="utf-8") as f:
                f.write("\n".join(armenia))
        if italia:
            with open("ITALIA.TXT", "w", encoding="utf-8") as f:
                f.write("\n".join(italia))
        if espania:
            with open("ESPAÑA.TXT", "w", encoding="utf-8") as f:
                f.write("\n".join(espania))

        print("Clasificación completada.")
    except FileNotFoundError:
        print("Error: el archivo especificado no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo de texto a procesar: ").strip()
    clasificar_apellidos(archivo)
