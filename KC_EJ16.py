# KC_EJ16
# Crear un programa que contenga una Lista de nombres.
# Solicitar un índice de la lista y mostrar el valor del índice.
# El programa deberá validar que el índice es válido.
# Ejemplo
# >>Lista predeterminada: “Pedro Picapiedra”, “Pablo Marmol”, “Bob Esponja”, “Patricio”
# >>Entrada: 2
# >>Salida: Bob Esponja

lista = ["Pedro Picapiedra", "Pablo Marmol", "Bob Esponja", "Patricio"]


def getIndiceLista(texto, lista):
    indiceMaximo = len(lista)-1
    while True:
        try:
            indice = int(input(texto))
            if 0 <= indice <= indiceMaximo:
                return indice
            else:
                print(
                    f"Índice no válido. Debe estar entre 0 y {indiceMaximo} (inclusive).")
        except ValueError:
            print("La entrada no es un número entero.")


print(f"Lista predeterminada: {lista}.")
indice = getIndiceLista("Introduzca un índice de la lista: ", lista)
print(f"Resultado: {lista[indice]}.")
