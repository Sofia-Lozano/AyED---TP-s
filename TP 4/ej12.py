#Ej 12
"""2. Escribir un programa para crear una lista por comprensión con los naipes de la baraja española.
La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla.
"""

palos = ["Oros", "Copas", "Espadas", "Bastos"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

baraja_española = [f"{numero} {palo}" for palo in palos for numero in numeros]

print("Baraja española:")
print(baraja_española)