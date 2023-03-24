import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QStackedLayout, QPushButton
from ControlColor import Color


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo Staked")

        caixaV = QVBoxLayout()
        caixaH = QHBoxLayout()

        btnVermello = QPushButton("Vermello")
        btnVermello.pressed.connect(self.activa_tarxeta_1)
        caixaH.addWidget(btnVermello)

        btnAzul = QPushButton("Azul")
        btnAzul.pressed.connect(self.activa_tarxeta_2)
        caixaH.addWidget(btnAzul)


        self.esquema = QStackedLayout()
        caixaV.addLayout(caixaH)
        caixaV.addLayout(self.esquema)

        self.esquema.addWidget(Color("red"))
        self.esquema.addWidget(Color("Yellow"))
        self.esquema.addWidget(Color("red"))

        self.esquema.setCurrentIndex(1)


        widget = QWidget()
        widget.setLayout(caixaV)
        self.setCentralWidget(widget)
        self.show()

    def activa_tarxeta_1(self):
        self.esquema.setCurrentIndex(0)

    def activa_tarxeta_2(self):
        self.esquema.setCurrentIndex(1)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
