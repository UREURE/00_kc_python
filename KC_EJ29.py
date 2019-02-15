# KC_EJ29
# Modificar el programa KC_EJ24 (promedio de alumnos) de forma tal que
# el cálculo del promedio se realice a través de una función.

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


def getPromedio(notas):
    return round(sum(notas)/len(notas))


calificaciones = []
while True:
    nombre = getNombre("Nombre de la persona (\"terminar\" para salir): ")
    if nombre.lower() == TERMINAR:
        break

    notas = []
    for i in range(0, 3):
        notas.append(getNota(f"Nota {i+1} de {nombre}: "))
    notaMedia = getPromedio(notas)
    calificaciones.append((nombre, notaMedia))

if len(calificaciones) == 0:
    print("Resultado: No se han introducido datos.")
else:
    calificaciones.sort(key=lambda c: c[1], reverse=True)
    textoResultado = ' '.join(f"{c[0]} {c[1]}" for c in calificaciones)
    print(f"Resultado: {textoResultado}.")
