import sys

from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QLineEdit, QHBoxLayout, QVBoxLayout, QTableView


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo Table Query')

        self.bd = QSqlDatabase("QSQLITE")
        self.bd.setDatabaseName("bbdd.dat")
        self.bd.open()

        caixaV = QVBoxLayout()
        caixaH = QHBoxLayout()

        self.tlvTaboa = QTableView()
        self.modelo = QSqlQueryModel()
        self.tlvTaboa.setModel(self.modelo)
        consulta = QSqlQuery("SELECT dni, nome, direccion FROM usuarios", db=self.bd)
        self.modelo.setQuery(consulta)
        self.modelo.setHeaderData(0, Qt.Orientation.Horizontal, "DNI")
        self.modelo.setHeaderData(1, Qt.Orientation.Horizontal, "NOME")
        self.modelo.setHeaderData(2, Qt.Orientation.Horizontal, "DIRECCION")


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
        consulta = QSqlQuery("SELECT dni, nome, direccion FROM usuarios WHERE dni= '" + self.bBuscar.text() + "'", db=self.bd)
        self.modelo.setQuery(consulta)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()
