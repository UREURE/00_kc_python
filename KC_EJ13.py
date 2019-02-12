# KC_EJ13
# Crear un programa que contenga una lista de 20 números y muestre un rango de la lista.
# El inicio y fin del rango serán introducidos por el usuario y el programa deberá validar
# que sean valores válidos.
# Ejemplo 1 (entrada no válida)
# >>Valores: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# >>Entradas: 11 y 23
# >>Salida: El rango debe ser de 1 a 20
# Ejemplo 2 (entrada válida)
# >>Valores: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# >>Entrada: 11 y 15
# >>Salida: 12, 13, 14, 15.

# Nota de alumno: tal como está descrito el ejercicio no se imprime nunca el valor "1".


def getNumero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("La entrada no es un número entero.")


rangoMinimo = 1
rangoMaximo = 21
valores = range(rangoMinimo, rangoMaximo)
textoValores = ', '.join(str(x) for x in valores)
print(f"Valores: {textoValores}")

n1 = getNumero("Introduzca el primer número: ")
n2 = getNumero("Introduzca el segundo número: ")

if n1 >= n2:
    print("El primer número debe ser inferior o igual al primero.")
elif n1 < rangoMinimo or n2 >= rangoMaximo:
    print(f"El rango debe ser de {rangoMinimo} a {rangoMaximo-1}.")
else:
    valoresEntreRango = valores[n1:n2]
    textoValoresEntreRango = ', '.join(str(x) for x in valoresEntreRango)
    print(f"Resultado: {textoValoresEntreRango}.")
