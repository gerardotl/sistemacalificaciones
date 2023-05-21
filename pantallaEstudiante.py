import pickle
from tkinter import messagebox
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




def agregarCalificacion(pcursos): 
    pcursos=pcursos
    cursos = pcursos   
    ventana2 = tk.Tk()
    ventana2.title("Agregar Calificaciones a Estudiante")
    ventana2.geometry("800x600")
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
    
    def agregarEstudiantesdesdeDB():
        
        conectar()
        con.conexion()
        lista = con.listarTodos()
        for item in lista:
            ncurso=item[1]
            print(type(ncurso))
            if ncurso in cursos:
               curso = cursos[ncurso]
            else:
                cursos[ncurso]=Curso(ncurso)
                curso=cursos[ncurso]
            # cursos[ncurso] = Curso(item[1])
            if len(curso.estudiantes) > 0:
                if estudiante.nombre == item[0]: 
                   estudiante = Estudiante(item[0])
                   estudiante.agregar_calificacion(item[1],item[2])
                else:
                    estudiante = Estudiante(item[0])
                    cursos[ncurso].agregar_estudiante(estudiante)
                    estudiante.agregar_calificacion(item[1],item[2])
            else:
                estudiante = Estudiante(item[0])
                cursos[ncurso].agregar_estudiante(estudiante)
                estudiante.agregar_calificacion(item[1],item[2])

    def agregarDatosTabla():
        cont=1
        lista=con.listarTodos()
        tabla.delete
        for i in tabla.get_children():
            tabla.delete(i)
        if len(lista)>0:
            for curso in lista:
                tabla.insert("", tk.END, text=str(cont), values=(curso[0], curso[1], curso[2]))
   
   
   
    agregarEstudiantesdesdeDB()   
        # lcursos=con.listar_cursos()
        # if len(lcursos) >0:
            
            
        #     for i in lcursos:
        #         cursos[i] = Curso(i)
        
    
    def getEstudiantes(eventObject):
        print("New Element Selected")
        comboEstudiante.set('')
        datos = con.listar_alumnos(combo.get())
        opEstudiante = [r for r, in datos]
        comboEstudiante['values']=opEstudiante

    def selectItem(a):
        curItem = tabla.focus()
        # print (tabla.item(curItem) )
        print(str(tabla.item(curItem).get('values')[0]))
        print(str(tabla.item(curItem).get('values')[1]))
        print(str(tabla.item(curItem).get('values')[2]))
        
        combo.set(tabla.item(curItem).get('values')[1])
        comboEstudiante.set(tabla.item(curItem).get('values')[0])
        txtcalificacion.delete(0,END)
        txtcalificacion.insert(0,str(tabla.item(curItem).get('values')[2]))
        # combo.setvar(tabla.item(curItem).get('values')[1]) 
        

    curs=tk.StringVar()

    etiqueta = tk.Label(agregarCalificacionFrame, text="Curso :")
    etiqueta.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    # Crear combobox y asignar opciones
    combo = Combobox(agregarCalificacionFrame, values=opCursos, textvariable=curs)
    combo.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    combo.bind('<<ComboboxSelected>>', getEstudiantes)
    label = Label(agregarCalificacionFrame, text="Alumno:")
    label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
    comboEstudiante = Combobox(agregarCalificacionFrame, values=opEstudiante)
    comboEstudiante.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    
    label = Label(agregarCalificacionFrame, text="Calificacion :")
    label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    
    txtcalificacion = Entry(agregarCalificacionFrame)
    txtcalificacion.grid(row=3, column=1, padx=5, pady=5)
    txtcalificacion.config(justify="left", state="normal")

    botonAgregar = Button(agregarCalificacionFrame, text="Agregar", command=lambda:agregar_calificacion(nombre_curso=combo.get(),nombre_estudiante=comboEstudiante.get(),calificacion=txtcalificacion.get()))
    botonAgregar.grid(row=4, column=0, padx=5, pady=5)

    botonAgregar = Button(agregarCalificacionFrame, text="Actualizar", command=lambda:actualizar_calificacion(nombre_curso=combo.get(),nombre_estudiante=comboEstudiante.get(),calificacion=txtcalificacion.get()))
    botonAgregar.grid(row=4, column=1, padx=5, pady=5)
    
    botonAgregar = Button(agregarCalificacionFrame, text="Eliminar", command=lambda:borrar_calificacion(nombre_curso=combo.get(),nombre_estudiante=comboEstudiante.get(),calificacion=txtcalificacion.get()))
    botonAgregar.grid(row=4, column=2, padx=5, pady=5)
    
    botonAgregar = Button(agregarCalificacionFrame, text="Mostrar Promedio", command=lambda:promedio(nombre_curso=combo.get(),nombre_estudiante=comboEstudiante.get(),calificacion=txtcalificacion.get()))
    botonAgregar.grid(row=4, column=3, padx=5, pady=5)
    

    tabla = ttk.Treeview(agregarCalificacionFrame)

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
    tabla.bind('<ButtonRelease-1>', selectItem)
    tabla.grid(row=5, column=2, padx=5, pady=5)
    
    agregarDatosTabla()
    
    agregarCalificacionFrame.pack()


    def agregar_calificacion(nombre_curso,nombre_estudiante,calificacion):
        try:
            curso = cursos[nombre_curso]
            for studiante in curso.estudiantes:
                if studiante.nombre == nombre_estudiante:
                    studiante.agregar_calificacion(nombre_curso, calificacion)
        
            
            conectar()

            con.actualizar(nombre=nombre_estudiante,curso=nombre_curso,calificacion=calificacion)
            
            fichero = open('estudiante.pckl','wb') # Escritura en modo binario, vacía el fichero si existe
            pickle.dump(list(cursos), fichero,protocol=0)      
            agregarDatosTabla()
            messagebox.showinfo("Informacion","Se agrego la calificacion")
            # agregarEstudiantesdesdeDB()
        except Exception as e:
            print(e)
            messagebox.showerror("Informacion","Error al agregar la calificacion")

    def borrar_calificacion(nombre_curso,nombre_estudiante,calificacion):
        try:
            conectar()
            con.eleminar(nombre=nombre_estudiante,curso=nombre_curso,calificacion=calificacion)
            agregarDatosTabla()
            combo.set('')
            comboEstudiante.set('')
            txtcalificacion.delete(0,END)
            
            messagebox.showinfo("Informacion","Se actualizo correctamente")
        except Exception as e:
            print(e)
            messagebox.showerror("Informacion","Error al eliminar ")
    def actualizar_calificacion(nombre_curso,nombre_estudiante,calificacion):
        try:
            conectar()
            con.actualizar(nombre=nombre_estudiante,curso=nombre_curso,calificacion=calificacion)
            agregarDatosTabla()
            messagebox.showinfo("Informacion","Se actualizo correctamente")

        except  Exception as e:
            print(e)

            messagebox.showerror("Informacion","Error al Actualizar")

    def promedio(nombre_curso,nombre_estudiante,calificacion):
            try:
                curso = cursos[nombre_curso]
                promedios = curso.obtener_promedios()
                messagebox.showinfo("Informacion","El promedio del curso es: " + str(promedios))

            except  Exception as e:
                print(e)
                messagebox.showerror("Informacion","Error calculando el promedio")

