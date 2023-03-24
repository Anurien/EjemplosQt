import sys

from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, \
    QLineEdit, QTextEdit, QRadioButton, QVBoxLayout, QHBoxLayout, QCheckBox, QGroupBox, QTabWidget, QComboBox, QSlider, \
    QLabel, QListView, QListWidget, QTableView


class ModeloTaboa(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self._datos = datos

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            return self._datos[indice.row()][indice.column()]

    def rowCount(self, index):
        return len(self._datos)

    def columnCount(self, indice):
        return len(self._datos[0])


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo Table')

        caixaV = QVBoxLayout()

        self.tlvTaboa = QTableView()
        caixaV.addWidget(self.tlvTaboa)

        contidoTaboa = [["Lunes", "Martes", "miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
                        [3, 5, 7, 2, 3, 0, 0],
                        [3, 2, 5, 7, 2, 3, 0]
                        ]
        self.modelo = ModeloTaboa(contidoTaboa)
        self.tlvTaboa.setModel(self.modelo)

        self.contedor = QWidget()
        self.contedor.setLayout(caixaV)

        self.setCentralWidget(self.contedor)
        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()
