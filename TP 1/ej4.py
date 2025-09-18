#Ej 4
"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""
def calcular_cambio(total_compra: int, dinero_recibido: int) -> None:
    """calcula el cambio a entregar, minimizando la cantidad de billetes.
    recibe como parámetros el total de la compra y el dinero recibido en forma de pago.
    verifica que el total de dinero recibido sea suficiente para abonar la compra e informa de un error si no se
    cuenta con la denominación de billetes necesaria para el vuelto.
    """
    if dinero_recibido < total_compra:
        print("Error: Dinero recibido insuficiente")
        return
    cambio = dinero_recibido - total_compra
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    cantidad_billetes = [0, 0, 0, 0, 0, 0, 0]
    for i, billete in enumerate(billetes):
        while cambio >= billete:
            cambio -= billete
            cantidad_billetes[i] += 1
    if cambio > 0:
        print("Error: No contamos con los billetes necesarios para entregar el cambio justo")
        pass
    print("Cambio:")
    for i, billete in enumerate(billetes):
        if cantidad_billetes[i] > 0:
            print(f"{cantidad_billetes[i]} billete(s) de ${billete}")

def main() -> None:
    """
    solicita al usuario el valor de la compra y la cantidad recibida como pago, utiliza la función calcular_cambio para verificar 
    e informa el resultado.
    """
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    calcular_cambio(total_compra, dinero_recibido)

if __name__ == "__main__":
    main()