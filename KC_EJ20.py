# KC_EJ20
# Crear un programa que escriba la suma de los números del 1 a N,
# donde N será dado por el usuario.
# Ejemplo
# >>Entrada: 8
# >>Salida: 1+2+3+4+5+6+7+8 = 36


def getNumero(texto):
    while True:
        try:
            n = int(input(texto))
            if n >= 1:
                return n
            else:
                print("Número no válido. Debe ser mayor que cero.")
        except ValueError:
            print("La entrada no es un número.")


n = getNumero("Introduzca un número: ")
numeros = range(1, n+1)

textoNumeros = '+'.join(str(x) for x in numeros)
sumaNumeros = sum(numeros)
print(f"Resultado: {textoNumeros} = {sumaNumeros}.")
