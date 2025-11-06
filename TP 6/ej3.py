#Ej 3

"""Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas,
leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas,
leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
"""

def grabar_rango_alturas(nombre_archivo: str) -> None:
    """
    Graba en un archivo las alturas de los atletas por disciplina.
    Cada disciplina se ingresa por teclado seguida de las alturas de sus atletas.
    El ingreso de disciplinas finaliza con una cadena vacía.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            while True:
                deporte = input("Ingrese el nombre del deporte (Enter para finalizar): ").strip()
                if deporte == "":
                    break
                f.write(deporte + "\n")
                while True:
                    altura = input(f"Ingrese una altura para {deporte} (Enter para pasar al siguiente deporte): ").strip()
                    if altura == "":
                        break
                    try:
                        valor = float(altura)
                        if valor <= 0:
                            print("La altura debe ser positiva.")
                            continue
                        f.write(str(valor) + "\n")
                    except ValueError:
                        print("Valor inválido. Ingrese una altura numérica válida.")
        print(f"Datos grabados correctamente en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al grabar los datos: {e}")


def grabar_promedio(nombre_entrada: str, nombre_salida: str) -> None:
    """
    Calcula el promedio de alturas por disciplina a partir del archivo de entrada
    y guarda los resultados en un nuevo archivo.
    """
    try:
        with open(nombre_entrada, "r", encoding="utf-8") as f:
            lineas = [linea.strip() for linea in f if linea.strip()]

        if not lineas:
            print("El archivo de entrada está vacío.")
            return

        with open(nombre_salida, "w", encoding="utf-8") as salida:
            i = 0
            while i < len(lineas):
                deporte = lineas[i]
                i += 1
                alturas = []
                while i < len(lineas):
                    try:
                        altura = float(lineas[i])
                        alturas.append(altura)
                        i += 1
                    except ValueError:
                        break
                if alturas:
                    promedio = sum(alturas) / len(alturas)
                    salida.write(f"{deporte}\n{promedio:.2f}\n")
        print(f"Promedios grabados correctamente en {nombre_salida}.")
    except FileNotFoundError:
        print("Error: el archivo de entrada no existe.")
    except Exception as e:
        print(f"Error al procesar los datos: {e}")


if __name__ == "__main__":
    archivo_alturas = "alturas.txt"
    archivo_promedios = "promedios.txt"

    print("=== Registro de alturas de atletas ===")
    grabar_rango_alturas(archivo_alturas)

    print("\n=== Cálculo de promedios ===")
    grabar_promedio(archivo_alturas, archivo_promedios)
