# KC_EJ30
# Crear un programa que simule una máquina expendedora de gaseosas con
# las siguientes características:
#  •Las bebidas disponibles son: Fanta, Pepsi, 7Up.
#  •Todas las bebidas tienen un costo de €1,0.
#  •La máquina recibe monedas de 10, 20 y 50 cent, y €1,0.
# El programa deberá permitir que el usuario seleccione una bebida e
# ingrese una a una las monedas.
# El programa deberá detenerse cuando el importe de la gaseosa haya sido completado y,
# de ser necesario, determinar el sobrante.

COSTE_BEBIDA = 1
bebidas = ("fanta", "pepsi", "7up")
monedas = {"10": 0.1, "20": 0.2, "50": 0.5, "1": 1}


def getBebida(texto):
    while True:
        bebida = input(texto).lower()
        if bebida in bebidas:
            return bebida
        else:
            print("Bebida no disponible. Bebidas disponibles:")
            print(bebidas)


def getMoneda(texto):
    while True:
        moneda = input(texto)
        if moneda in monedas:
            return monedas[moneda]
        else:
            print("Moneda no válida. Monedas válidas:")
            print(monedas)


bebida = getBebida("Introduzca qué bebida desea: ")
insertado = 0
while insertado < COSTE_BEBIDA:
    mensaje = f"Introduzca el importe (faltan {round(COSTE_BEBIDA-insertado, 1)}€): "
    insertado += getMoneda(mensaje)

if insertado > COSTE_BEBIDA:
    print(f"Tome su cambio ({round(insertado-COSTE_BEBIDA, 1)}€).")

print(f"Muchas gracias, disfrute de su {bebida}.")
