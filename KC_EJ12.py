# KC_EJ12
# Crear un programa que reciba una letra e indique si es vocal o consonante.
# Ejemplo
# >>Entrada: E
# >>Salida: E es letra vocal

vocales = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú")


def getLetra(texto):
    while True:
        letra = input(texto)
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Letra no válida. Introduzca una única letra.")


letra = getLetra("Introduzca una letra: ")
clasificacion = "vocal" if letra.lower() in vocales else "consonante"
print(f"Resultado: {letra} es letra {clasificacion}.")
