# KC_EJ15
# Crear un programa que reciba el nombre y las calificaciones de 3 personas.
# Para cada persona deberá guardar la información en una tupla.
# El programa no mostrará resultados de salida.


def getNombre(texto):
    while True:
        nombre = input(texto)
        if len(nombre) > 0:
            return nombre
        else:
            print("Nombre vacío, no es válido.")


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


calificaciones = []
for i in range(3):
    nombre = getNombre(f"Introduzca el nombre de la persona {i+1}: ")
    nota = getNota(f"Introduzca la nota de {nombre}: ")
    calificaciones.append((nombre, nota))
