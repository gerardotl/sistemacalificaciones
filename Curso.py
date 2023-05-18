
from json import JSONEncoder


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def obtener_promedios(self):
        promedios = []
        for estudiante in self.estudiantes:
            promedio = estudiante.obtener_promedio()
            promedios.append((estudiante.nombre, promedio))
        promedios.sort(key=lambda x: x[1], reverse=True)
        return promedios

