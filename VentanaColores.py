import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

from ControlColor import Color


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QVBoxLayout")
        caixaV = QVBoxLayout()
        caixaV.setContentsMargins(0,0,0,0)
        caixaV.setSpacing(0)
        caixaV.addWidget(Color("red"))
        caixaV.addWidget(Color("Yellow"))
        caixaV.addWidget(Color("red"))

        caixaH = QHBoxLayout()
        caixaH.setContentsMargins(0, 0, 0, 0)
        caixaH.setSpacing(0)
        caixaH.addWidget(Color("red"))
        caixaH.addWidget(Color("Yellow"))
        caixaH.addWidget(Color("red"))


        widget = QWidget()
        widget.setLayout(caixaV)

        widget = QWidget()
        widget.setLayout(caixaH)
        self.setCentralWidget(widget)
        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
