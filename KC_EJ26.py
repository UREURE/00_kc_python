# KC_EJ26
# Crear un programa con una función pintar_fila() que arme las filas de una tabla html.
# Completar el programa con la estructura de una tabla e invocando a la función N veces,
# donde N es un valor introducido por el usuario.
# Ejemplo
# >>Entrada: 4
# >>Salida:
# <table>
#   #ciclo invocando 4 veces a la función pintar_fila()
#   <tr><td></td></tr>
#   <tr><td></td></tr>
#   <tr><td></td></tr>
#   <tr><td></td></tr>
#   #- - - fin ciclo
# </table>


def getNumero(texto):
    while True:
        try:
            n = int(input(texto))
            if n > 0:
                return n
            else:
                print("Número no válido. Debe ser mayor que cero.")
        except ValueError:
            print("La entrada no es un número.")


def pintar_fila():
    return "<tr><td></td></tr>"


nFilas = getNumero("Introduzca el número de filas: ")

print("<table>")
for i in range(0, nFilas):
    print(f"\t{pintar_fila()}")

print("</table>")
