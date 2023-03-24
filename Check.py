import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QRadioButton, QButtonGroup


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Check ventana en Python")

        self.home = QCheckBox("Hombre")
        self.muller = QCheckBox("Mujer")

        self.h = QRadioButton("Hombre")
        self.h.toggled.connect(self.on_option_toggled)
        self.m = QRadioButton("Mujer")
        self.m.toggled.connect(self.on_option_toggled)

        self.f = QRadioButton("Furro")
        self.f.toggled.connect(self.on_option_toggled)
        self.nf = QRadioButton("No furro")
        self.nf.toggled.connect(self.on_option_toggled)

        self.muller.setCheckState(Qt.CheckState.Checked)
        self.muller.stateChanged.connect(self.on_boton_clicked1)

        self.home.setCheckState(Qt.CheckState.Checked)
        self.home.stateChanged.connect(self.on_boton_clicked)

        self.caixaV = QVBoxLayout()

        self.caixaV.addWidget(self.home)
        self.caixaV.addWidget(self.muller)
        self.caixaV.addWidget(self.m)
        self.caixaV.addWidget(self.h)
        self.caixaV.addWidget(self.f)
        self.caixaV.addWidget(self.nf)

        self.contedor = QWidget()
        self.contedor.setLayout(self.caixaV)

        grupoXenero = QButtonGroup(self.contedor)
        grupoXenero.addButton(self.m)
        grupoXenero.addButton(self.h)
        grupoFurro = QButtonGroup(self.contedor)
        grupoFurro.addButton(self.f)
        grupoFurro.addButton(self.nf)

        self.setCentralWidget(self.contedor)

        self.show()

    def on_boton_clicked(self, estado):
        print("El boton fue pulsado")
        #self.home.setCheckState(Qt.CheckState.Checked)
        if self.muller.isChecked():
            self.muller.setCheckState(Qt.CheckState.Unchecked)

    def on_boton_clicked1(self, estado):
        print("El boton fue pulsado")
        if self.home.isChecked():
            self.home.setCheckState(Qt.CheckState.Unchecked)
        #self.muller.setCheckState(Qt.CheckState.Checked)

    def on_option_toggled(self):
        print("Seleccionado: ", self.sender().isChecked(),"Nome: ",self.sender().text())


#Para que la ventana este sincronizado con el sistema operativo o algo asi
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
