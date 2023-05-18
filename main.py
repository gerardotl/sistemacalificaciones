from tkinter.ttk import Combobox
from Estudiante import Estudiante
from Curso import Curso
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
cursos = {}

ventana = tk.Tk()
ventana.title("Calificaciones")
ventana.geometry("500x500")
estd =[]

def agregar_estudiante(nombre_curso,nombre_estudiante):
    if nombre_curso not in cursos:
        cursos[nombre_curso] = Curso(nombre_curso)
        estudiante = Estudiante(nombre_estudiante)
        cursos[nombre_curso].agregar_estudiante(estudiante)
        print(list(cursos))
        ##json_data = json.dump(cursos.__dict__())
        # with open("cursos.json", "w") as jsonfile:
        #     json.dump(cursos, jsonfile)


def agregarEstudiante():    
    ventana1 = tk.Tk()
    ventana1.title("Agregar Curso y Estudiante")
    ventana1.geometry("700x400")
    agregarEstudianteFrame=Frame(ventana1)
   
    #empaquetamos el frame a la ventana principal
    agregarEstudianteFrame.pack(side=RIGHT, anchor="n")#Side permite especificar la ubicación del Frame en pantalla
    agregarEstudianteFrame.pack(fill="x",expand=1)#Expand y fill es para poder especificar el frame dentro
    #agregamos un tamaño al frame
    agregarEstudianteFrame.config(width=600,height=300)
    #cambiar de cursor
    agregarEstudianteFrame.config(cursor="pirate") 
    label = Label(agregarEstudianteFrame, text="Nombre Curso:")
    label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    
    curso = Entry(agregarEstudianteFrame)
    curso.grid(row=0, column=1, padx=5, pady=5)
    curso.config(justify="left", state="normal")

    label1 = Label(agregarEstudianteFrame, text="Nombre Estudiante:")
    label1.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    estudiante = Entry(agregarEstudianteFrame)
    estudiante.grid(row=1, column=1, padx=5, pady=5)
    estudiante.config(justify="left", state="normal")
    
    botonAgregar = Button(agregarEstudianteFrame, text="Agregar", command=lambda:agregar_estudiante(curso.get(),estudiante.get()))
    botonAgregar.grid(row=3, column=1, padx=5, pady=5)

    agregarEstudianteFrame.pack()

def getEstudiantes(nombrecurso):
    estd = cursos.get(nombrecurso)

def invoke_Setting_Group(self, event):  
    estd = cursos.get('Curso 1')

def agregarCalificaciones():
    ventana2 = tk.Tk()
    ventana2.title("Agregar Calificaciones a Estudiante")
    ventana2.geometry("700x400")
    agregarCalificacionFrame=Frame(ventana2)
    #empaquetamos el frame a la ventana principal
    agregarCalificacionFrame.pack(side=RIGHT, anchor="n")#Side permite especificar la ubicación del Frame en pantalla
    agregarCalificacionFrame.pack(fill="x",expand=1)#Expand y fill es para poder especificar el frame dentro
    #agregamos un tamaño al frame
    agregarCalificacionFrame.config(width=600,height=300)
    #cambiar de cursor
    agregarCalificacionFrame.config(cursor="pirate") 
    # Crear etiqueta para mostrar el resultado de la selección
    etiqueta = tk.Label(agregarCalificacionFrame, text="Curso :")
    etiqueta.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    # Definir opciones de la lista desplegable
    opCurso = []
    opEstudiante = []
    
    for nombre,estudiantes in cursos.items():
        print(nombre)
        opCurso.append(nombre)
        

        
    

    # Crear combobox y asignar opciones
    combo = Combobox(agregarCalificacionFrame, values=opCurso)
    combo.bind("<<ComboboxSelected>>", lambda event:invoke_Setting_Group(self, event))
    combo.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    label = Label(agregarCalificacionFrame, text="Calificacion:")
    label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    comboEstudiante = Combobox(agregarCalificacionFrame, values=estd)
    comboEstudiante.bind("<<ComboboxSelected>>", lambda event:invoke_Setting_Group(self, event))
    comboEstudiante.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    agregarCalificacionFrame.pack()

barraMenu=Menu(ventana)
ventana.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)
archivoEstudiante=Menu(barraMenu,tearoff=0)
# archivoCalificacion=Menu(barraMenu,tearoff=0)
# archivoEdicion=Menu(barraMenu,tearoff=0)
# archivoHerramientas=Menu(barraMenu,tearoff=0)
# archivoAyuda=Menu(barraMenu,tearoff=0)

# #menus a la barra
# barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
# barraMenu.add_cascade(label="Eición",menu=archivoEdicion)
# barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
# barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

# #Submenus de menu archivo
# archivoMenu.add_command(label="Nuevo")
# archivoMenu.add_command(label="Guardar")
# archivoMenu.add_command(label="Guardar Como")
# archivoMenu.add_separator()
# archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
# archivoMenu.add_command(label="Salir",command=estadoSalir)

# #Submenus de menu edicion
# archivoEdicion.add_command(label="Copiar")
# archivoEdicion.add_command(label="Cortar")
# archivoEdicion.add_command(label="Pegar")

# #Submenus de menu ayuda
# archivoAyuda.add_command(label="Licencia",command=estadoLicencia)
# archivoAyuda.add_command(label="Acerca de",command=infoAdicional)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Estudiante",menu=archivoEstudiante)
archivoEstudiante.add_command(label='Agregar Curso',command=agregarEstudiante)
archivoEstudiante.add_command(label='Agregar Estudiante',command=agregarCalificaciones)
archivoEstudiante.add_command(label='Calcular Promedio')
archivoEstudiante.add_command(label='Guardar un archivo')
archivoEstudiante.add_command(label='Leer datos de archivo')

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

