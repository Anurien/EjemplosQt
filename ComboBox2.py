import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, \
    QLineEdit, QTextEdit, QRadioButton, QVBoxLayout, QHBoxLayout, QCheckBox, QGroupBox, QTabWidget, QComboBox, QSlider, \
    QLabel, QListView, QListWidget


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo QComboBox')

        caixaV = QVBoxLayout()

        # LineEdit
        self.cuadroTexto = QLineEdit()
        self.cuadroTexto.setPlaceholderText("Escribe aquÃ­")
        self.cuadroTexto.returnPressed.connect(self.on_cuadroTexto_returnPressed)
        caixaV.addWidget(self.cuadroTexto)

        # Combo
        self.combo = QComboBox()
        self.combo.addItems(["Hombre", "Mujer", "No Binario"])
        self.combo.currentIndexChanged.connect(self.on_combo_currentIndexChanged)
        self.combo.currentTextChanged.connect(self.on_combo_currentTextChanged)
        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        caixaV.addWidget(self.combo)

        # Lista
        self.lista = QListWidget()
        self.lista.addItems(["Hombre", "Mujer", "No Binario"])
        self.lista.currentItemChanged.connect(self.on_lista_currentIndexChanged)
        self.lista.currentTextChanged.connect(self.on_lista_currentTextChanged)
        caixaV.addWidget(self.lista)

        self.contedor = QWidget()
        self.contedor.setLayout(caixaV)

        self.setCentralWidget(self.contedor)
        self.show()

    def on_combo_currentIndexChanged(self, indice):
        print(indice)
        print(self.combo.itemText(indice))

    def on_combo_currentTextChanged(self, texto):
        print(texto)

    def on_lista_currentIndexChanged(self, indice):
        print(indice)

    def on_lista_currentTextChanged(self, texto):
        print(texto)

    def on_cuadroTexto_returnPressed(self):
        self.lista.addItem(self.cuadroTexto.text())
        self.cuadroTexto.setText(" ")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()