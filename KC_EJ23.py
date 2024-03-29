# KC_EJ23
# Crear un programa que reciba los el nombre y las calificaciones de N personas,
# mientras que el usuario no escriba “terminar”.
# Al terminar deberá mostrar la media de calificaciones de cada persona.
# Ejemplo
# >>Entradas:
# Pedro 6, 8, 7
# Pablo 9, 9, 10
# Bob 10, 10, 10
# terminar
# >>Salida:
# Pedro 7
# Pablo 9
# Bob 10

TERMINAR = "terminar"


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
while True:
    nombre = getNombre("Nombre de la persona (\"terminar\" para salir): ")
    if nombre.lower() == TERMINAR:
        break

    sumaNotas = 0
    for i in range(0, 3):
        sumaNotas += getNota(f"Nota {i+1} de {nombre}: ")
    notaMedia = round(sumaNotas / 3)
    calificaciones.append((nombre, notaMedia))

if len(calificaciones) == 0:
    print("Resultado: No se han introducido datos.")
else:
    print("Resultado:")
    for c in calificaciones:
        print(f"\t{c[0]} {c[1]}.")
