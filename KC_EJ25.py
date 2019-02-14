# KC_EJ25
# Crear un programa que contenga un número aleatorio del 1 al 100,
# sin mostrarlo, y permitir que el usuario intente adivinarlo.
# El usuario solamente tendrá 5 oportunidades, en cada oportunidad fallida
# se le darán pistas para saber si debe intentar con un número mayor o menor.
# Ejemplo
# >>Número a adivinar: 32
#  •Entrada: 10
#  •Salida: Intenta con un número mayor (te quedan 4 oportunidades)
#  •Entrada: 40
#  •Salida: Intenta con un número menor (te quedan 3 oportunidades)
#  •Entrada: 35
#  •Salida: Intenta con un número menor (te quedan 2 oportunidades)
#  •Entrada: 32
#  •Salida: ¡Bien, has adivinado! :D

import random


def getNumero(texto):
    while True:
        try:
            n = int(input(texto))
            if 1 <= n <= 100:
                return n
            else:
                print("Número no válido. Debe estar entre 1 y 100 (inclusive).")
        except ValueError:
            print("La entrada no es un número.")


n = random.randint(1, 100)
nUsuario = 0
mensaje = "Adivina el número secreto: "

i = 5
while i > 0:
    nUsuario = getNumero(mensaje)
    if n == nUsuario:
        print("¡Bien, has adivinado! :D")
        break
    mensajeMayorOMenor = "mayor" if nUsuario < n else "menor"
    mensaje = f"Intenta con un número {mensajeMayorOMenor} (te quedan {i-1} oportunidades): "
    i -= 1

if n != nUsuario:
    print("No te ha dado tiempo.")
    print(f"El número secreto era: {n}.")
    print("Vuelve a intentarlo, a ver si tienes más suerte la próxima vez ;)")
