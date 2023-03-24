import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, \
    QLineEdit, QTextEdit, QRadioButton, QVBoxLayout, QHBoxLayout, QCheckBox, QGroupBox, QTabWidget, QComboBox, QSlider, \
    QLabel, QListView


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Swing')
        self.setGeometry(300, 300, 350, 200)

        caixaV = QVBoxLayout()
        caixaH = QHBoxLayout()
        boton = QPushButton('boton')
        caixaH.addWidget(boton)
        checkBox = QCheckBox('checkBox')
        caixaH.addWidget(checkBox)
        caixaV.addLayout(caixaH)

        caixaH2 = QHBoxLayout()
        caixaV.addLayout(caixaH2)
        caixaV1 = QVBoxLayout()
        caixaH2.addLayout(caixaV1)
        grid = QGridLayout()

        self.rb1 = QRadioButton('RadioButton 1')
        self.rb2 = QRadioButton('RadioButton 2')
        self.rb3 = QRadioButton('RadioButton 3')
        self.rb4 = QRadioButton('RadioButton 4')
        self.cerrar = QPushButton('cerrar')

        grid.addWidget(QListView(), 0, 0, 7, 1)
        grid.addWidget(self.rb1, 0, 1)
        grid.addWidget(self.rb2, 1, 1)
        grid.addWidget(self.rb3, 2, 1)
        grid.addWidget(self.rb4, 3, 1)
        grid.addWidget(self.cerrar, 6, 1)

        # contedor = QWidget()
        # contedor.setLayout(grid)

        caixaG = QGroupBox('GroupBox')
        caixaG.setLayout(grid)
        caixaV1.addWidget(caixaG)

        cadroTexto1 = QLineEdit()
        caixaV1.addWidget(cadroTexto1)
        cadroTexto2 = QLineEdit()
        caixaV1.addWidget(cadroTexto2)
        combo = QComboBox()
        caixaV1.addWidget(combo)

        caixaV2 = QVBoxLayout()
        caixaH2.addLayout(caixaV2)
        grid = QGridLayout()
        casa1 = QCheckBox('1')
        casa2 = QCheckBox('2')
        casa3 = QCheckBox('3')
        deslizador = QSlider(Qt.Orientation.Horizontal)
        grid.addWidget(casa1, 0, 0)
        grid.addWidget(casa2, 1, 0)
        grid.addWidget(casa3, 2, 0)
        grid.addWidget(QWidget())
        grid.addWidget(deslizador, 5, 0, 1, 2)

        contedor1 = QWidget()
        contedor1.setLayout(grid)
        tab = QTabWidget()
        tab.addTab(contedor1, 'solapa1')
        tab.addTab(QLabel("texto sola2"), 'solapa2')
        caixaV2.addWidget(tab)
        areaTexto = QTextEdit()
        caixaV2.addWidget(areaTexto)


        self.contedor = QWidget()
        self.contedor.setLayout(caixaV)
        self.contedor.setGeometry(200, 100, 200, 100)
        self.setCentralWidget(self.contedor)

        self.show()

        # buttons


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()
