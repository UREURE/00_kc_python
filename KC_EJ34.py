# KC_EJ34
# Crear las clases AlumnoRemoto y AlumnoPresencial,
# ambas subclases de la clase Alumno creada en el ejercicio KC_EJ31.
# >>AlumnoRemoto deberá contar con los atributos numero_matricula, nombre,
# apellido, correo_electronico, estatus_inscrito, skype, huso_horario.
# >>Mientras que AlumnoPresencial deberá definir los atributos numero_matricula,
# nombre, apellido, correo_electronico, estatus_inscrito, numero_asiento.


class Alumno():
    def __init__(self, matricula, nombre, apellido, email, inscrito):
        self.__numero_matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo_electronico = email
        self.__estatus_inscrito = inscrito

    def getNombre(self):
        return self.__nombre


class AlumnoRemoto(Alumno):
    def __init__(self, matricula, nombre, apellido, email, inscrito, skype, huso_horario):
        super().__init__(matricula, nombre, apellido, email, inscrito)
        self.__skype = skype
        self.__huso_horario = huso_horario


class AlumnoPresencial(Alumno):
    def __init__(self, matricula, nombre, apellido, email, inscrito, numero_asiento):
        super().__init__(matricula, nombre, apellido, email, inscrito)
        self.__numero_asiento = numero_asiento


aR = AlumnoRemoto(1, "Juan", "González", "jgl@el.es", True, "jgl.skype.es", -5)
aP = AlumnoPresencial(1, "Pedro", "Ramírez Pérez", "prp@el.es", True, 12)

print(f"Alumno remoto: {aR.getNombre()}.")
print(f"Alumno presencial: {aP.getNombre()}.")
