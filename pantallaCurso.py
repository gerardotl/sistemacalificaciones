from tkinter.ttk import Combobox
from Estudiante import Estudiante
from Curso import Curso
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk

from BD_Conectar import BD_Conectar

cursos = {}
con=BD_Conectar()
def conectar():
    con.conexion()
 
def agregar_estudiante(nombre_curso,nombre_estudiante):
    if nombre_curso not in cursos:
        cursos[nombre_curso] = Curso(nombre_curso)
        estudiante = Estudiante(nombre_estudiante)
        cursos[nombre_curso].agregar_estudiante(estudiante)
        print(list(cursos))
        conectar()
        con.insertar(nombre_estudiante,nombre_curso)
        ##json_data = json.dump(cursos.__dict__())
        # with open("cursos.json", "w") as jsonfile:
        #     json.dump(cursos, jsonfile)


def agregarEstudiante(cursos):
    cursos = cursos    
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


