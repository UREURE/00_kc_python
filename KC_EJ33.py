# KC_EJ33
# Usando las clases de los ejercicios KC_EJ31 y KC_EJ32,
# crear un programa que contenga una instancia de la clase Módulo,
# con instancias de alumnos predefinidos en init.
# El programa permitirá al usuario:
# >>Ver todos los alumnos enrolados.
# >>Buscar un alumno por matrícula.

import datetime


class Alumno():
    def __init__(self, matricula, nombre, apellido, email):
        self.__numero_matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo_electronico = email
        self.__estatus_inscrito = True

    def getNumeroMatricula(self):
        return self.__numero_matricula

    def getNombre(self):
        return self.__nombre

    def getEstatusInscrito(self):
        return self.__estatus_inscrito


class Modulo():
    def __init__(self):
        self.__listado_alumnos = []
        self.__fechaInicio = datetime.date(1900, 1, 1)
        self.__fechaFin = datetime.date(1900, 1, 1)

        self.__listado_alumnos.append(
            Alumno(1, "Juan", "González López", "jgl@el.es"))
        self.__listado_alumnos.append(
            Alumno(1, "Pedro", "Ramírez Pérez", "prp@el.es"))
        self.__listado_alumnos.append(
            Alumno(1, "Marta", "González López", "jgl@el.es"))

    def agregarAlumno(self, alumno):
        self.__listado_alumnos.append(alumno)

    def buscarAlumnoNombre(self, nombreAlumno):
        return [x for x in self.__listado_alumnos if x.getNombre().lower() == nombreAlumno.low()]

    def buscarAlumnoMatricula(self, numeroMatricula):
        return [x for x in self.__listado_alumnos if x.getNumeroMatricula() == numeroMatricula]

    def getAlumnosInscritos(self, nombreAlumno):
        return [x for x in self.__listado_alumnos if x.__estatus_inscrito()]
