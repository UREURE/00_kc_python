# KC_EJ06
# Crea un programa que solicite dos números y muestre los resultados de aplicar
# comparaciones relacionales.
# Ejemplo
# >>Entradas 30 y 2
# >>Salida:
# 30 < 2 = False
# 30 > 2 = True
# 30 y 2 son iguales = False
# 30 y 2 son distintos = True


def getNumero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("La entrada no es un número entero.")


n1 = getNumero("Intoduzca el primer número: ")
n2 = getNumero("Intoduzca el segundo número: ")

print(f"{n1} < {n2} = {n1<n2}")
print(f"{n1} > {n2} = {n1>n2}")
print(f"{n1} y {n2} son iguales = {n1==n2}")
print(f"{n1} y {n2} son distintos = {n1!=n2}")
