#Ej 3

"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""

from typing import Tuple

def dividir_correo(correo: str) -> Tuple[str, ...]:
    """
    Recibe una dirección de correo electrónico y devuelve una tupla con sus partes:
    (usuario, dominio, subdominio, extensión, ...)
    Devuelve una tupla vacía si el formato es inválido.
    """
    if "@" not in correo or correo.count("@") != 1:
        return ()
    usuario, dominio_completo = correo.split("@")
    if not usuario or "." not in dominio_completo:
        return ()
    partes = [usuario] + dominio_completo.split(".")
    if any(not parte for parte in partes):
        return ()
    return tuple(partes)


def main() -> None:
    correo = input("Ingrese una dirección de correo electrónico: ").strip()
    partes = dividir_correo(correo)
    if partes:
        print("Partes del correo:", partes)
    else:
        print("Formato de correo inválido.")


if __name__ == "__main__":
    main()
