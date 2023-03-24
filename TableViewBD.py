import sys

from PyQt6 import QtGui
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtCore import Qt, QAbstractTableModel, QSize
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, \
    QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QLabel, QListView, QListWidget, QTableView


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo Table BD')

        bd = QSqlDatabase("QSQLITE")
        bd.setDatabaseName("bbdd.dat")
        bd.open()

        caixaV = QVBoxLayout()
        caixaH = QHBoxLayout()

        self.tlvTaboa = QTableView()
        self.modelo = QSqlTableModel(db=bd)
        self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.tlvTaboa.setModel(self.modelo)
        self.modelo.setTable("usuarios")
        self.modelo.setSort(0, Qt.SortOrder.DescendingOrder)
        self.modelo.setHeaderData(0, Qt.Orientation.Horizontal, "DNI")
        self.modelo.setHeaderData(1, Qt.Orientation.Horizontal, "NOME")
        self.modelo.setHeaderData(2, Qt.Orientation.Horizontal, "DIRECCION")
        #self.modelo.removeColumns(2, 1)
        self.modelo.select()

        self.bGuardar = QPushButton("Actualizar BD")
        self.bGuardar.clicked.connect(self.on_bGuardar_pressed)

        self.bCancelar = QPushButton("Cancelar")
        self.bCancelar.clicked.connect(self.on_bCancelar_pressed)

        self.bBuscar = QLineEdit()
        self.bBuscar.setPlaceholderText("BuscarDNI")
        self.bBuscar.returnPressed.connect(self.on_bBuscar_pressed)

        self.setMinimumSize(800, 600)
        caixaV.addWidget(self.tlvTaboa)
        caixaH.addWidget(self.bGuardar)
        caixaH.addWidget(self.bCancelar)
        caixaV.addWidget(self.bBuscar)
        caixaV.addLayout(caixaH)

        self.contedor = QWidget()
        self.contedor.setLayout(caixaV)

        self.setCentralWidget(self.contedor)
        self.show()

    def on_bGuardar_pressed(self):
        self.modelo.submitAll()

    def on_bCancelar_pressed(self):
        self.modelo.revertAll()

    def on_bBuscar_pressed(self):
        filtro = 'dni= "{}"'.format(self.bBuscar.text())
        self.modelo.setFilter(filtro)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()
