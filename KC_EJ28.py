# KC_EJ28
# Crear un programa que contenga una función pintar_rectangulo(lado, figura).
# Esta función deberá pintar en consola un cuadrilátero de lado x lado con
# la figura proporcionada.
# Ejemplo:
# >>Entrada: lado 10, figura +
# >>Salida:
#  ++++++++++
# +                 +
# +                 +
# +                 +
# +                 +
# +                 +
# +                 +
# +                 +
# +                 +
# ++++++++++


def getFigura(texto):
    while True:
        figura = input(texto)
        if len(figura) == 1:
            return figura
        else:
            print("Figura no válida. Introduzca un único caracter.")


def getLado(texto):
    while True:
        try:
            n = int(input(texto))
            if 1 < n < 81:
                return n
            else:
                print("Lado no válido. Debe estar entre 2 y 80 (inclusive).")
        except ValueError:
            print("La entrada no es un número.")


def pintar_rectangulo(lado, figura):
    exterior = figura*lado
    interior = " "*(lado-2)

    print(exterior)
    for i in range(0, lado-2):
        print(f"{figura}{interior}{figura}")
    print(exterior)


l = getLado("Introduzca la longitud del lado: ")
f = getFigura("Introduzca el caracter de la figura: ")
pintar_rectangulo(l, f)
