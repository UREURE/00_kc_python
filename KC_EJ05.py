# KC_EJ05
# Crear un programa que solicite el año y mes de nacimiento de dos personas,
# y muestre el resultado de compararlas
# Ejemplo
# >>Entradas:
# mes 1 Enero
# año 1 1980
# mes 2 Febrero
# año 2 1980
# >>Salida: False

meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre",
         "diciembre")


def getMes(texto):
    while True:
        mes = input(texto)
        if (mes.lower() in meses):
            return mes
        else:
            print("El mes no es válido. Meses disponibles:")
            print(meses)


def getAnio(texto):
    while True:
        try:
            anio = int(input(texto))
            if 1900 < anio < 2020:
                return anio
            else:
                print("Año no válido. Debe estar entre 1900 y 2020 (exclusive).")
        except ValueError:
            print("La entrada no es un número entero.")


mesPer1 = getMes("Introduzca el mes de la primera persona: ")
anioPer1 = getAnio("Introduzca el año de la primera persona: ")
mesPer2 = getMes("Introduzca el mes de la segunda persona: ")
anioPer2 = getAnio("Introduzca el año de la segunda persona: ")

iguales = mesPer1.lower() == mesPer2.lower() and anioPer1 == anioPer2

print(iguales)
