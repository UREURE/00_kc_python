# KC_EJ04
# Crea un programa que solicite tres notas y muestre su media.
# Ejemplo
# >>Entradas: 8, 9 y 6
# >>Salida: La media es 7.6


def getNota(texto):
    while True:
        try:
            nota = float(input(texto))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota no válida. Debe estar entre 0 y 10 (inclusive).")
        except ValueError:
            print("La entrada no es un número.")


notas = []
for i in range(3):
    notas.append(getNota(f"Introduzca la nota {i+1}: "))

media = sum(notas) / len(notas)
print("La media es", round(media, 1))
