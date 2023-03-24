import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QLabel


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primera ventana en Python")
        self.pulsado = 0

        self.label = QLabel("")
        self.boton = QPushButton("Pulsame")


        self.boton.clicked.connect(self.on_boton_clicked)

        self.caixaV=QVBoxLayout()
        self.caixaV.addWidget(self.boton)
        self.caixaV.addWidget(self.label)
        
        self.contedor = QWidget()
        self.contedor.setLayout(self.caixaV)

        self.setCentralWidget(self.contedor)

        self.show()


    def on_boton_clicked(self):
        print("El boton fue pulsado")
        self.pulsado = self.pulsado + 1
        self.label.setText("El boton fue pulsado: "+str(self.pulsado))

        QMessageBox.information(self, 'Evento', 'El boton fue pulsado')






'''Para que la ventana este sincronizado con el sistema operativo o algo asi'''
aplicacion = QApplication(sys.argv)
ventana = VentanaPrincipal()
aplicacion.exec()
