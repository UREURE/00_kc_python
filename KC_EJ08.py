# KC_EJ08
# Crear un programa que reciba un número entero y muestre si es par o impar,
# positivo o negativo, o cero.
# Ejemplo:
# >>Entrada: 23
# >>Salida: Positivo impar.


def getNumero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("La entrada no es un número entero.")


n = getNumero("Intoduzca un número: ")
if n == 0:
    print("El número es cero.")
else:
    signo = "Positivo" if n > 0 else "Negativo"
    paridad = "Par" if n % 2 == 0 else "impar"
    print(f"Resultado: {signo} {paridad}.")
