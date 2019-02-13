# KC_EJ22
# Crear un programa que reciba los nombres y edades de 10 personas.
# Mostrar únicamente los nombres de las personas que tienen derecho a votar
# (mayores a 18 años).
# Ejemplo
# >>Entradas: Pedro 23, Bob 15, Patricio 7, Pablo 30, Betty 20, Pebbles 2 ...
# >>Salida: Tienen derecho al voto Pedro, Pablo y Betty.


def getNombre(texto):
    while True:
        nombre = input(texto)
        if len(nombre) > 0:
            return nombre
        else:
            print("Nombre vacío, no es válido.")


def getEdad(texto):
    while True:
        try:
            edad = int(input(texto))
            if 1 <= edad <= 110:
                return edad
            else:
                print("Edad no válida. Debe estar entre 1 y 110 (inclusive).")
        except ValueError:
            print("La entrada no es un número.")


personas = []
for i in range(10):
    nombre = getNombre(f"Introduzca el nombre de la persona {i+1}: ")
    edad = getEdad(f"Introduzca la edad de {nombre}: ")
    personas.append((nombre, edad))

personasMayoresEdad = [x for x in personas if x[1] > 17]
textoVotantes = ', '.join(x[0] for x in personasMayoresEdad)
print(f"Tienen derecho a voto: {textoVotantes}.")
