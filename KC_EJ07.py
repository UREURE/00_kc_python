# KC_EJ07
# Crea un programa que solicite tres notas y calcule su media.
# Dependiendo del valor de la media, mostrará si el resultado es Apto o No Apto.
# Ejemplo
# >>Entradas: 10, 9 y 9
# >>Salida: Apto


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
resultado = "Apto" if media >= 5 else "No Apto"
print("Resultado:", resultado)
