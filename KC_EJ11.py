# KC_EJ11
# Crear un programa que reciba 3 números e indique cuál es el mayor y el menor.
# Ejemplo
# >>Entradas: 5, 19 y 2
# >>Salida: El mayor es 19, el menor es 2


def getNumero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("La entrada no es un número entero.")


lista = []
lista.append(getNumero("Introduzca el primer número: "))
lista.append(getNumero("Introduzca el segundo número: "))
lista.append(getNumero("Introduzca el tercer número: "))
lista.sort()

print(f"El mayor es {lista[-1]}, el menor es {lista[0]}.")
