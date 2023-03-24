import sys

from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, \
    QLineEdit, QTextEdit, QRadioButton, QVBoxLayout, QHBoxLayout, QCheckBox, QGroupBox, QTabWidget, QComboBox, QSlider, \
    QLabel, QListView, QListWidget

tick = QtGui.QImage('Yes_Check_Circle.svg.png')


class ModeloListaTareas(QAbstractListModel):
    def __init__(self, lista=None):
        super().__init__()
        self.lista = lista or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            estado, texto = self.lista[indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado, texto = self.lista[indice.row()]
            if estado:
                return QImage.scaled(tick, 15, 15)

    def rowCount(self, index):
        return len(self.lista)


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo Lista')

        caixaV = QVBoxLayout()

        # Lista
        self.modelo = ModeloListaTareas([(False, "A miña primeira tarefa")])
        self.lista = QListView()
        self.lista.setModel(self.modelo)
        # self.lista = QListWidget()
        # self.lista.addItems(["Hombre", "Mujer", "No Binario"])
        # self.lista.currentItemChanged.connect(self.on_lista_currentIndexChanged)
        # self.lista.currentTextChanged.connect(self.on_lista_currentTextChanged)
        caixaV.addWidget(self.lista)

        # LineEdit
        self.cuadroTexto = QLineEdit()
        self.cuadroTexto.setPlaceholderText("Escribe aqui")
        self.cuadroTexto.returnPressed.connect(self.on_cuadroTexto_returnPressed)
        caixaV.addWidget(self.cuadroTexto)

        # Botones
        caixaH = QHBoxLayout()
        caixaV.addLayout(caixaH)
        self.bBorrar = QPushButton("Borrar")
        caixaH.addWidget(self.bBorrar)
        self.bBorrar.pressed.connect(self.on_button_borrar_pressed)

        self.bFeito = QPushButton("Feito")
        caixaH.addWidget(self.bFeito)
        self.bFeito.pressed.connect(self.on_button_feito_pressed)

        self.bEngadir = QPushButton("Engadir")
        caixaV.addWidget(self.bEngadir)
        self.bEngadir.pressed.connect(self.on_button_engadir_pressed)

        self.contedor = QWidget()
        self.contedor.setLayout(caixaV)

        self.setCentralWidget(self.contedor)
        self.show()

    def on_lista_currentIndexChanged(self, indice):
        print(indice)

    def on_lista_currentTextChanged(self, texto):
        print(texto)

    def on_cuadroTexto_returnPressed(self):
        # self.lista.addItem(self.cuadroTexto.text())
        # self.cuadroTexto.setText(" ")
        # el nombredel QlineEdit el mio es cuadroTexto
        novaTarefa = self.cuadroTexto.text()
        novaTarefa = novaTarefa.strip()
        if novaTarefa:
            self.modelo.lista.append((False, novaTarefa))
            # Para que la tabla se haga mas grande cuando añades
            self.modelo.layoutChanged.emit()
            self.cuadroTexto.setText("")

    def on_button_borrar_pressed(self):
        # self.lista.editItem(self.cuadroTexto.text())
        indices = self.lista.selectedIndexes()
        if indices:
            indice = indices[0]
            del self.modelo.lista[indice.row()]
            # self.modelo.listaTareas.remove(self.modelo.listaTareas[indice.row()])
            self.modelo.layoutChanged.emit()
            self.lista.clearSelection()

    def on_button_feito_pressed(self):
        indices = self.lista.selectedIndexes()
        if indices:
            indice = indices[0]
            fila = indice.row()
            estado, descripcionTarea = self.modelo.lista[fila]
            self.modelo.lista[fila] = (True, descripcionTarea)
            self.modelo.dataChanged.emit(indice, indice)
            self.lista.clearSelection()

    def on_button_engadir_pressed(self):
        novaTarefa = self.cuadroTexto.text()
        novaTarefa = novaTarefa.strip()
        if novaTarefa:
            self.modelo.lista.append((False, novaTarefa))
            # Para que la tabla se haga mas grande cuando añades
            self.modelo.layoutChanged.emit()
            self.cuadroTexto.setText("")




if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()
