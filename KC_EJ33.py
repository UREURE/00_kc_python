# KC_EJ33
# Usando las clases de los ejercicios KC_EJ31 y KC_EJ32,
# crear un programa que contenga una instancia de la clase Módulo,
# con instancias de alumnos predefinidos en init.
# El programa permitirá al usuario:
# >>Ver todos los alumnos enrolados.
# >>Buscar un alumno por matrícula.

import datetime


class Alumno():
    def __init__(self, matricula, nombre, apellido, email, inscrito):
        self.__numero_matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo_electronico = email
        self.__estatus_inscrito = inscrito

    def getNumeroMatricula(self):
        return self.__numero_matricula

    def getNombre(self):
        return self.__nombre

    def getEstatusInscrito(self):
        return self.__estatus_inscrito


class Modulo():
    def __init__(self, fechaInicio, fechaFin):
        self.__listado_alumnos = []
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin

        self.__listado_alumnos.append(
            Alumno(1, "Juan", "González López", "jgl@el.es", True))
        self.__listado_alumnos.append(
            Alumno(2, "Pedro", "Ramírez Pérez", "prp@el.es", True))
        self.__listado_alumnos.append(
            Alumno(3, "Marta", "González López", "jgl@el.es", True))

    def agregarAlumno(self, alumno):
        self.__listado_alumnos.append(alumno)

    def buscarAlumnoNombre(self, nombreAlumno):
        return [x for x in self.__listado_alumnos if x.getNombre().lower() == nombreAlumno.lower()]

    def buscarAlumnoMatricula(self, numeroMatricula):
        return [x for x in self.__listado_alumnos if x.getNumeroMatricula() == numeroMatricula]

    def getAlumnosInscritos(self):
        return [x for x in self.__listado_alumnos if x.getEstatusInscrito()]


fechaInicio = datetime.date(2019, 1, 1)
fechaFin = datetime.date(2019, 12, 31)
modulo = Modulo(fechaInicio, fechaFin)

inscritos = modulo.getAlumnosInscritos()
print(f"Hay {len(inscritos)} alumno(s) inscrito(s).")

alN = modulo.buscarAlumnoNombre("Juan")
print(f"{alN[0].getNombre()} tiene matrícula {alN[0].getNumeroMatricula()}.")

alM = modulo.buscarAlumnoMatricula(2)
print(f"El matriculado {alM[0].getNumeroMatricula()} es {alM[0].getNombre()}.")

print(f"Alumnos inscritos:")
alI = modulo.getAlumnosInscritos()
for x in alI:
    print(f"\t{x.getNombre()}.")
