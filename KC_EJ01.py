# KC_EJ01
# Crea un programa por el cual se solicite al usuario el radio de un círculo.
# El programa deberá calcular y mostrar el área.
# Ejemplo
# >>Entrada: 5
# >>Salida: El radio es 78.5

import math

radioCorrecto = False
while not radioCorrecto:
    try:
        radio = float(input("Radio: "))
        radioCorrecto = radio > 0
        if not radioCorrecto:
            print("El radio debe ser un número mayor que cero.")
    except ValueError:
        print("La entrada no es un número.")

area = math.pi * radio**2
print("El radio es", round(area, 1))
