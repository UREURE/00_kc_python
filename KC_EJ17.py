# KC_EJ17
# Crear un programa que contenga un diccionario con nombres y correos electrónicos.
# Solicitar el nombre de una persona y mostrar su correo electrónico.
# Indicar con un mensaje apropiado cuando no se encuentre un resultado válido.
# Ejemplo
# >>Diccionario predeterminado: Pedro - pedro.picapiedra@gmail.com Pablo - pmarmol123@gmail.com Bob - bob@gmail.com
# >>Entrada: Pablo
# >>Salida: pmarmol123@gmail.com

dicc = {"Pedro": "pedro.picapiedra@gmail.com",
        "Pablo": "pmarmol123@gmail.com",
        "Bob": "bob@gmail.com"}


def getNombreDiccionario(texto, dicc):
    while True:
        nombre = input(texto)
        if nombre in dicc:
            return nombre
        else:
            print("Nombre no encontrado. Respete mayúsculas y minúsculas.")


print("Diccionario predeterminado:")
for key, value in dicc.items():
    print(f"  {key} - {value}.")
nombre = getNombreDiccionario("Introduzca un nombre del diccionario: ", dicc)
print(f"Resultado: {dicc[nombre]}.")
