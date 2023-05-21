from Estudiante import Estudiante
from Curso import Curso
import json
import tkinter as tk
from tkinter import *

from pantallaCurso import agregarEstudiante
from pantallaEstudiante import agregarCalificacion, agregarCalificaciones

cursos = {}
    
ventana = tk.Tk()
ventana.title("Calificaciones")
ventana.geometry("800x600")

barraMenu=Menu(ventana)
ventana.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)
archivoEstudiante=Menu(barraMenu,tearoff=0)

# #Submenus de menu ayuda
# archivoAyuda.add_command(label="Licencia",command=estadoLicencia)
# archivoAyuda.add_command(label="Acerca de",command=infoAdicional)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Estudiante",menu=archivoEstudiante)
archivoEstudiante.add_command(label='Agregar Curso',command=lambda:agregarEstudiante(cursos=cursos))
archivoEstudiante.add_command(label='CRUD Estudiante',command=lambda:agregarCalificacion(pcursos=cursos))


ventana.mainloop()


while True:
    print("1. Agregar estudiante a un curso")
    print("2. Agregar calificación a un estudiante")
    print("3. Calcular promedio de calificaciones de cada estudiante y mostrar lista ordenada")
    print("4. Guardar un archivo")
    print("5. Leer datos de archivo")
    
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_curso = input("Ingrese el nombre del curso: ")
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")

        if nombre_curso not in cursos:
            cursos[nombre_curso] = Curso(nombre_curso)

        estudiante = Estudiante(nombre_estudiante)
        cursos[nombre_curso].agregar_estudiante(estudiante)
        print(list(cursos))
        ##json_data = json.dump(cursos.__dict__())
        with open("cursos.json", "w") as jsonfile:
            json.dump(cursos, jsonfile)


    elif opcion == "2":
        nombre_curso = input("Ingrese el nombre del curso: ")
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        calificacion = float(input("Ingrese la calificación: "))

        curso = cursos[nombre_curso]
        for estudiante in curso.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                estudiante.agregar_calificacion(nombre_curso, calificacion)
        
        with open("cursos.json", "w") as jsonfile:
            json.dumps(cursos.__dict__, jsonfile)

    elif opcion == "3":
        nombre_curso = input("Ingrese el nombre del curso: ")
        curso = cursos[nombre_curso]
        promedios = curso.obtener_promedios()
        
        print(f"Promedio de calificaciones para el curso {nombre_curso}:")
        for estudiante, promedio in promedios:
            print(f"{estudiante}: {promedio}")

    
    elif opcion == "5":
        break

    else:
        print("Opción inválida")

