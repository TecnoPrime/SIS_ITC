import sys
import typing
from PyQt5.QtWidgets import QApplication, QDialog,QLineEdit,QPushButton,QTableWidget, QTableWidgetItem, QWidget,QMessageBox
from PyQt5 import QtCore, QtGui, uic
import logica

class CursosIU(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("IndiceCursos.ui", self)
        self.curso= logica.Curso()
        self.btnConsultar.clicked.connect(self.ConsultarFiltro)
        self.nuevoCursoIU=NuevoCursoIU()
        self.btnNuevo.clicked.connect(self.abrirNuevoCurso)
        self.btnEliminar.clicked.connect(self.eliminarCurso)
        self.indice=0
    def eliminarCurso(self):
        self.indice=self.Lista.currentRow()
        ID=self.Lista.item(self.indice,0).text()
        pregunta=QMessageBox.question(self,"Eliminar Curso", "¿Esta seguro de eliminar el curso?{}".format(self.Lista.item(self.indice,1).text()),QMessageBox.Yes|QMessageBox.No)
        if pregunta==QMessageBox.Yes:
            self.curso.eliminar(ID)
            self.ConsultarFiltro()
    def abrirNuevoCurso(self):
        self.nuevoCursoIU.show()
    def ConsultarFiltro(self):
        nomb=self.txtConsultar.text()
        lista=self.curso.listarXNombre(nomb)
        self.CargarCursos(lista)
    def showEvent(self, event):
        lista=self.curso.listar()
        self.CargarCursos(lista)
    def CargarCursos(self, lista):
        filas=len(lista)
        self.Lista.setRowCount(filas)
        indice=0
        for c in lista:
            self.Lista.setItem(indice,0,QTableWidgetItem(str(c[0])))
            self.Lista.setItem(indice,1,QTableWidgetItem(c[1]))
            self.Lista.setItem(indice,2,QTableWidgetItem(str(c[2])))
            self.Lista.setItem(indice,3,QTableWidgetItem(c[3]))
            indice+=1
class NuevoCursoIU(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('NuevoCurso.ui',self)
        self.btnCancelar.clicked.connect(self.cerrar)
        self.curso=logica.Curso()
        self.btnGuardar.clicked.connect(self.guardar)
    def showEvent(self, event):
        self.txtNombre.setText("")
        self.txtCosto.setText("")
        self.txtDetalle.setText("")
    def guardar(self):
        nomb=self.txtNombre.text()
        costo=int(self.txtCosto.text())
        detalle=self.txtDetalle.text()
        self.curso.crear(nomb, costo, detalle)
        self.close()
        self.curso.crear()
    def cerrar(self):
        self.close()

app=QApplication(sys.argv)
IndiceCursosIU=CursosIU()
IndiceCursosIU.show()
app.exec_()