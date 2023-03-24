import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QPushButton, \
    QLineEdit


class CreateWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('calculadora')

        self.text = '0'

        # layout

        grid = QGridLayout()

        # show numbers
        self.resultText = QLineEdit(self.text)
        self.resultText.setReadOnly(True)
        self.resultText.setStyleSheet('background: #7FFFD4;')

        # buttons
        self.but9 = QPushButton('9')
        self.but8 = QPushButton('8')
        self.but7 = QPushButton('7')
        self.but6 = QPushButton('6')
        self.but5 = QPushButton('5')
        self.but4 = QPushButton('4')
        self.but3 = QPushButton('3')
        self.but2 = QPushButton('2')
        self.but1 = QPushButton('1')
        self.but0 = QPushButton('0')

        # positionate the buttons

        grid.addWidget(self.but9, 1, 2)
        grid.addWidget(self.but8, 1, 1)
        grid.addWidget(self.but7, 1, 0)
        grid.addWidget(self.but6, 2, 2)
        grid.addWidget(self.but5, 2, 1)
        grid.addWidget(self.but4, 2, 0)
        grid.addWidget(self.but3, 3, 2)
        grid.addWidget(self.but2, 3, 1)
        grid.addWidget(self.but1, 3, 0)
       # grid.addWidget(self.but0, 4, 0, 1, 3)

        contedormaia = QWidget()
        contedormaia.setLayout(grid)

        caixaV = QVBoxLayout()
        caixaV.setSpacing(0)
        caixaV.setContentsMargins(0, 0, 0, 5)
        caixaV.addWidget(contedormaia)
        caixaV.addWidget(self.but0)

        teclasoperacions = QGridLayout()
        teclasoperacions.addWidget(QPushButton("+"), 0, 3)
        teclasoperacions.addWidget(QPushButton("-"), 1, 3)
        teclasoperacions.addWidget(QPushButton("/"), 2, 3)
        teclasoperacions.addWidget(QPushButton("x"), 3, 3)
        teclasoperacions.addWidget(QPushButton("="), 4, 3)

        caixaH = QHBoxLayout()
        caixaH.addLayout(caixaV)
        caixaH.addLayout(teclasoperacions)

        contedor = QWidget
        contedor.setLayout(caixaH)
        self.setCentralWidget(contedor)

        self.show()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CreateWindow()
    aplicacion.exec()
