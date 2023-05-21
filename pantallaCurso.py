import pickle
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

def agregarEstudiante(cursos):
    cursos = cursos    
    ventana1 = tk.Tk()
    ventana1.title("Agregar Curso y Estudiante")
    ventana1.geometry("800x600")
    agregarEstudianteFrame=Frame(ventana1)
    
    #empaquetamos el frame a la ventana principal
    agregarEstudianteFrame.pack(side=RIGHT, anchor="n")#Side permite especificar la ubicación del Frame en pantalla
    agregarEstudianteFrame.pack(fill="x",expand=1)#Expand y fill es para poder especificar el frame dentro
    #agregamos un tamaño al frame
    agregarEstudianteFrame.config(width=600,height=300)
    #cambiar de cursor
    
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

    def agregarDatosTabla():
            cont=1
            lista=con.listarTodos()
            tabla.delete
            for i in tabla.get_children():
                tabla.delete(i)
            if len(lista)>0:
                for curso in lista:
                    tabla.insert("", tk.END, text=str(cont), values=(curso[0], curso[1], curso[2]))
            
            lcursos=con.listar_cursos()
            if len(lcursos) >0:
                for i in lcursos:
                    cursos[i] = Curso(i)
                    



    
    tabla = ttk.Treeview(agregarEstudianteFrame)

    # Definir columnas
    tabla["columns"] = ("Curso", "Nombre", "Calificacion")
    
    # Formato de las columnas
    tabla.column("#0", width=0, stretch=tk.NO)  # Columna invisible
    tabla.column("Curso", anchor=tk.W, width=150)
    tabla.column("Nombre", anchor=tk.CENTER, width=70)
    tabla.column("Calificacion", anchor=tk.W, width=200)

    # Encabezados de las columnas
    tabla.heading("#0", text="")
    tabla.heading("Curso", text="Curso")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Calificacion", text="Calificacion")

    # Agregar datos a la tabla
    #tabla.insert("", tk.END, text="1", values=("John Doe", 30, "johndoe@example.com"))
    #tabla.insert("", tk.END, text="2", values=("Jane Smith", 25, "janesmith@example.com"))
    
    tabla.grid(row=4, column=1, padx=5, pady=5)
    
    agregarDatosTabla()
    agregarEstudianteFrame.pack()

    
    def agregar_estudiante(nombre_curso,nombre_estudiante):
        if nombre_curso not in cursos:
            cursos[nombre_curso] = Curso(nombre_curso)
            estudiante = Estudiante(nombre_estudiante)
            cursos[nombre_curso].agregar_estudiante(estudiante)
            print(list(cursos))
        else:
            curso = cursos[nombre_curso]
            if nombre_estudiante not in curso.estudiantes:
               estudiante = Estudiante(nombre_estudiante)
               cursos[nombre_curso].agregar_estudiante(estudiante)

        conectar()
        con.insertar(nombre_estudiante,nombre_curso)
            # with open("cursos.json", "w") as jsonfile:
            #     json.dump(cursos, jsonfile)
            
        fichero = open('estudiante.pckl','wb') # Escritura en modo binario, vacía el fichero si existe
        pickle.dump(list(cursos), fichero,protocol=0)      


        agregarDatosTabla()



