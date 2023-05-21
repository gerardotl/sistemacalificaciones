import sqlite3
class BD_Conectar:
    #Crear conexion BD

    
    #Crear cursor
    #cursor=miConexion.cursor()
    id_recibe=0
    
    def __init__(self) -> None:
        pass

    def conexion(self):
        print("Si pase conectado")
        miConexion=sqlite3.connect("calificaciones.sqlite")
        cursor=miConexion.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS ESTUDIANTE (NOMBRE VARCHAR(25), CURSO VARCHAR(25), CALIFICACION REAL)")
        miConexion.commit()
        miConexion.close()
    
    #INSERTAR DATOS
    def insertar(self,nombre,curso,calificacion=0):
        miConexion=sqlite3.connect("calificaciones.sqlite")
        cursor=miConexion.cursor()

        datos=(nombre,curso,calificacion)
        sql="INSERT INTO ESTUDIANTE VALUES(?,?,?)"
        cursor.execute(sql,datos)
        miConexion.commit()
        miConexion.close()
    #LISTAR REGISTROS
    def listar_cursos(self):
      
        miConexion=sqlite3.connect("calificaciones.sqlite")
        cursor=miConexion.cursor()
        cursor.execute("SELECT DISTINCT	CURSO FROM ESTUDIANTE")
        listaRegistros=cursor.fetchall()
        print("Datos listados")
        miConexion.commit()
        miConexion.close()
        return listaRegistros
    
    def listar_alumnos(self,nombreCurso):
        miConexion=sqlite3.connect("calificaciones.sqlite")
        cursor=miConexion.cursor()
        cursor.execute("SELECT DISTINCT NOMBRE FROM ESTUDIANTE WHERE CURSO='"+nombreCurso+"'")
        listaRegistros=cursor.fetchall()
        print("Datos listados")
        miConexion.commit()
        miConexion.close()
        return listaRegistros
   
   #LISTAR REGISTROS
    def listarTodos(self):
        miConexion=sqlite3.connect("calificaciones.sqlite")
        cursor=miConexion.cursor()
        cursor.execute("SELECT * FROM ESTUDIANTE")
        listaRegistros=cursor.fetchall()
        print("Datos listados")
        miConexion.commit()
        miConexion.close()
        return listaRegistros
    
    #ACTUALIZAR REGISTRO
    def actualizar(self,nombre,curso, calificacion):

        miConexion=sqlite3.connect("calificaciones.sqlite")
        cursor=miConexion.cursor()
        sql ="UPDATE ESTUDIANTE SET NOMBRE = '"+nombre+"', CURSO= '"+curso+"', CALIFICACION= "+ calificacion + " WHERE CURSO = '"  +curso + "' AND  NOMBRE = '" +nombre +"'"
        cursor.execute(sql)
        print("El registro ha sido actualizas")
        miConexion.commit()
        miConexion.close()

    #ELIMAR REGISTRO
    def eleminar(self,nombre,curso,calificacion):
        miConexion=sqlite3.connect("calificaciones.sqlite")
        cursor=miConexion.cursor()
        sql ="DELETE FROM ESTUDIANTE WHERE CURSO = '"  +curso + "' AND  NOMBRE = '" +nombre +"' AND CALIFICACION =" + calificacion
        cursor.execute(sql)
        # cursor.execute("DELETE FROM ESTUDIANTE WHERE NOMBRE="+nombre+"")
        print("El registro ha sido eliminado")
        miConexion.commit()
        miConexion.close()

