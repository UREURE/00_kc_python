# KC_EJ31
# Crear una clase Alumno con los siguientes atributos:
# >>numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito.
# La matrícula deberá ser numérica, mientras que correo_electronico,
# nombre y apellido como textos.
# El atributo estatus_inscrito deberá ser un valor booleano.


class Alumno():
    def __init__(self, matricula, nombre, apellido, email):
        self.__numero_matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo_electronico = email
        self.__estatus_inscrito = True
