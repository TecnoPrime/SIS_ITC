import sqlite3

class Curso:
    def __init__(self):
        self.cnn=sqlite3.connect("BD.db")
    def listar(self):
        cursor=self.cnn.execute("SELECT * FROM CURSOS")
        return cursor.fetchall()
    def listarXNombre(self, nomb):
        cursor=self.cnn.execute("SELECT * FROM CURSOS WHERE NOMBRE LIKE '%{}%'".format(nomb))
        return cursor.fetchall()
    def crear(self,nomb,costo,detalle):
        cursor=self.cnn.execute("INSERT INTO CURSOS(NOMBRE, COSTO, DETALLE) VALUES('{}','{}','{}')".format(nomb,costo,detalle))
        self.cnn.commit()
    def actualizar(self, ID, nomb):
        cursor=self.cnn.execute("UPDATE CURSOS SET NOMBRE='{}' WHERE CURSOID='{}'".format(nomb,ID))
        self.cnn.commit()
    def eliminar(self, ID):
        cursor=self.cnn.execute("DELETE FROM CURSOS WHERE CURSOID='{}'".format(ID))
        self.cnn.commit()