import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, \
    QLineEdit, QTextEdit


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Excel')
        self.setGeometry(300, 300, 350,200)

        self.text = 'Hoja 1'+'\n'+' Hoja 2'+ '\n'+'Hoja 3'

        # layout

        grid = QGridLayout()

        # show numbers
        self.resultText = QTextEdit(self.text)
       # self.resultText = QLineEdit(self.text)
        self.resultText.setReadOnly(True)

        self.resultText1 = QTextEdit(self.text)
        self.resultText1.setReadOnly(True)

        # buttons
        self.ocultar = QPushButton('ocultar')
        self.mostrar = QPushButton('mostrar')
        self.cerrar = QPushButton('cerrar')

        # positionate the buttons
        grid.addWidget(self.ocultar, 0, 1, 2, 1)
        grid.addWidget(self.mostrar, 1, 1, 2, 1)
        grid.addWidget(self.cerrar, 4, 3, 1, 1)
        grid.addWidget(self.resultText, 0, 0, 3, 1)
        grid.addWidget(self.resultText1, 0, 3, 3, 1)
        grid.setContentsMargins(10, 10, 10,10)
        grid.setSpacing(20)


        self.contedor = QWidget()
        self.contedor.setLayout(grid)
        self.contedor.setGeometry(200, 100, 200, 100)

        self.setCentralWidget(self.contedor)

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()
