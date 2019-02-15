# KC_EJ27
# Crear un programa que contenga una función es_palindromo(texto) y
# determine si dicho texto es un palíndromo.
# Ejemplo
# >>Entrada: anita lava la tina
# >>Salida: El texto ingresado ES palíndromo


def getFrase(texto):
    while True:
        frase = input(texto)
        if len(frase) > 2:
            return frase
        else:
            print("Frase demasiado corta, no es válida.")


def es_palindromo(texto):
    fMin = f.lower()
    fMinSinEsp = fMin.replace(" ", "")
    trans = str.maketrans("áéíóúü", "aeiouu")
    fMinSinEspNiAcen = fMinSinEsp.translate(trans)
    fMinSinEspNiAcenReves = fMinSinEspNiAcen[::-1]
    return fMinSinEspNiAcen == fMinSinEspNiAcenReves


f = getFrase("Inroduzca una frase: ")
esPalindromo = es_palindromo(f)
textoResultado = "ES" if esPalindromo else "NO es"
print(f"El texto ingresado {textoResultado} palíndromo.")
