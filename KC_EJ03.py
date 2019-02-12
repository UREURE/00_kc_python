# KC_EJ03
# Crea un programa que solicite una cantidad en Euros y
# muestre su equivalente en USD.
# Ejemplo
# >>Entrada: 10.0
# >>Salida: $10.06 USD

CAMBIO_EURO_DOLAR = 1.13


def getNumero(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("La entrada no es un número.")


euros = getNumero("Euros: ")
print(f"Conversión: ${round(euros*CAMBIO_EURO_DOLAR, 2)} USD")
