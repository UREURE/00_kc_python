# KC_EJ02
# Crea un programa que solicite dos números y muestre los resultados de todas
# sus operaciones aritméticas.
# Ejemplo
# >>Entradas: 30 y 2
# >>Salida:
# 30+2 = 32
# 30-2 = 28
# 30x2= 60
# 30/2 = 15
# 30**2 = 900
# 30%2 = 0


def getNumero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("La entrada no es un número entero.")


n1 = getNumero("Intoduzca el primer número: ")
n2 = getNumero("Intoduzca el segundo número: ")

if n2 != 0:
    division = n1/n2
    modulo = n1 % n2
else:
    division = modulo = "División entre cero"

print(f"{n1}+{n2} = {n1+n2}")
print(f"{n1}-{n2} = {n1-n2}")
print(f"{n1}x{n2} = {n1*n2}")
print(f"{n1}/{n2} = {division}")
print(f"{n1}**{n2} = {n1**n2}")
print(f"{n1}%{n2} = {modulo}")
