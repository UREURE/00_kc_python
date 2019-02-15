# KC_EJ32
# Crear una clase Módulo con los siguientes atributos:
# >>Listado_alumnos, fecha_inicio, fecha_fin.
# El listado de alumnos deberá ser tipo Lista y contener objetos de tipo Alumno creado en el ejercicio KC_EJ31.
# En la misma clase Módulo deberá implementar métodos para
# >>agregar objetos Alumno a la Lista
# >>buscar un alumno
# >>mostrar todos los alumnos con estatus_inscrito == True.

import datetime


class Alumno():
    def __init__(self, matricula, nombre, apellido, email):
        self.__numero_matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo_electronico = email
        self.__estatus_inscrito = True

    def getNombre(self):
        return self.__nombre

    def getEstatusInscrito(self):
        return self.__estatus_inscrito


class Modulo():
    def __init__(self):
        self.__listado_alumnos = []
        self.__fechaInicio = datetime.date(1900, 1, 1)
        self.__fechaFin = datetime.date(1900, 1, 1)

    def agregarAlumno(self, alumno):
        self.__listado_alumnos.append(alumno)

    def buscarAlumno(self, nombreAlumno):
        return [x for x in self.__listado_alumnos if x.getNombre().lower() == nombreAlumno.low()]

    def getAlumnosInscritos(self, nombreAlumno):
        return [x for x in self.__listado_alumnos if x.__estatus_inscrito()]
