from tkinter.ttk import Combobox
from Estudiante import Estudiante
from Curso import Curso
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk

from BD_Conectar import BD_Conectar

cursos = {}

opCursos = []
opEstudiante = []

con=BD_Conectar()
def conectar():
    con.conexion()

def agregarCalificaciones():
        for nombre,estudiantes in cursos.items():
            print(nombre)
            opCursos.append(nombre)




def agregarCalificacion(cursos): 
    cursos = cursos   
    ventana2 = tk.Tk()
    ventana2.title("Agregar Calificaciones a Estudiante")
    ventana2.geometry("700x400")
    estud=tk.StringVar()


    

    agregarCalificacionFrame=Frame(ventana2)
        #empaquetamos el frame a la ventana principal
    agregarCalificacionFrame.pack(side=RIGHT, anchor="n")#Side permite especificar la ubicación del Frame en pantalla
    agregarCalificacionFrame.pack(fill="x",expand=1)#Expand y fill es para poder especificar el frame dentro
    #agregamos un tamaño al frame
    agregarCalificacionFrame.config(width=600,height=300)
    
    conectar()
    con.conexion()
    datos= con.listar_cursos()
    opCursos = [r for r, in datos]
    
    def getEstudiantes(eventObject):
        print("New Element Selected")
        comboEstudiante.set('')
        datos = con.listar_alumnos(combo.get())
        opEstudiante = [r for r, in datos]
        comboEstudiante['values']=opEstudiante

    curs=tk.StringVar()

    etiqueta = tk.Label(agregarCalificacionFrame, text="Curso :")
    etiqueta.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    # Crear combobox y asignar opciones
    combo = Combobox(agregarCalificacionFrame, values=opCursos, textvariable=curs)
    combo.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    combo.bind('<<ComboboxSelected>>', getEstudiantes)
    label = Label(agregarCalificacionFrame, text="Calificacion:")
    label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
    comboEstudiante = Combobox(agregarCalificacionFrame, values=opEstudiante)
    comboEstudiante.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    #comboEstudiante.bind('<<ComboboxSelected>>', getEstudiantes)
    
    #comboEstudiante.bind('<Button-1>', getEstudiantes)
    agregarCalificacionFrame.pack()

    #curs.trace('w',getEstudiantes)
    
    
