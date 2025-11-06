#Ej 4
"""Desarrollar un programa para eliminar todos los comentarios de un programa escrito
en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
y que también se considera comentario a las cadenas de documentación
(docstrings).
"""

import io
import tokenize

def eliminar_comentarios(nombre_entrada: str, nombre_salida: str) -> None:
    """
    Elimina todos los comentarios y cadenas de documentación (docstrings)
    de un archivo Python, generando un nuevo archivo limpio.
    """
    try:
        with open(nombre_entrada, "r", encoding="utf-8") as entrada:
            codigo = entrada.read()

        tokens = tokenize.generate_tokens(io.StringIO(codigo).readline)
        resultado = []

        for tipo, token, _, _, _ in tokens:
            if tipo == tokenize.COMMENT:
                continue
            if tipo == tokenize.STRING:
                if not resultado or resultado[-1][0] == tokenize.INDENT:
                    continue
            resultado.append((tipo, token))

        codigo_limpio = tokenize.untokenize(resultado)

        with open(nombre_salida, "w", encoding="utf-8") as salida:
            salida.write(codigo_limpio)

        print(f"Archivo limpio generado: {nombre_salida}")

    except FileNotFoundError:
        print("Error: el archivo especificado no existe.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


if __name__ == "__main__":
    archivo_entrada = input("Ingrese el nombre del archivo Python a limpiar: ").strip()
    archivo_salida = input("Ingrese el nombre del archivo de salida: ").strip()
    eliminar_comentarios(archivo_entrada, archivo_salida)
