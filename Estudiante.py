class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = {}

    def agregar_calificacion(self, curso, calificacion):
        self.calificaciones[curso] = calificacion

    def obtener_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)
        

        
    
        

