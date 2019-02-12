# KC_EJ09
# Crea un programa que reciba una cantidad,
# y pregunte si desea convertirla de Euros a USD o de USD a Euros y
# muestre el resultado de la conversión.
# Ejemplo
# >>Entradas:
#   •Cantidad 10.0
#   •Opción Euros a USD
# >>Salida: $10.06 USD


CAMBIO_EURO_DOLAR = 1.13
opciones = ("Euros a USD", "USD a Euros")
conversiones = ("euros a usd", "usd a euros")


def getNumero(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("La entrada no es un número.")


def getConversion(texto):
    while True:
        conversion = input(texto)
        if (conversion.lower() in conversiones):
            return conversion
        else:
            print("La conversión no es válida. Conversiones disponibles:")
            print(opciones)


importe = getNumero("Cantidad: ")
conversion = getConversion(f"Opción {opciones}: ")

if conversion.lower() == conversiones[0]:
    print(f"Conversión: ${round(importe*CAMBIO_EURO_DOLAR, 2)} USD")
else:
    print(f"Conversión: {round(importe/CAMBIO_EURO_DOLAR, 2)}€")
