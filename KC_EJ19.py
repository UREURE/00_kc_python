# KC_EJ19
# Crear un programa que almacene 10 números dados por el usuario y
# muestre únicamente los pares.
# Ejemplo
# >>Entrada: 10, 3, 6, 12, 20, 5, 9, 7, 11, 40
# >>Salida: Son pares 10, 6, 12, 20, 40.


def getNumero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("La entrada no es un número entero.")


pares = []
for i in range(0, 10):
    n = getNumero(f"Introduzca el número {i+1}: ")
    if n % 2 == 0 and not n in pares:
        pares.append(n)

if len(pares) > 0:
    textoPares = ', '.join(str(x) for x in pares)
    print(f"Resultado: Son pares {textoPares}.")
else:
    print("Resultado: no hay números pares.")
