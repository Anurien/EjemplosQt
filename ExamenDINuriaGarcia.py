import sys
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QLabel, QCheckBox, QTextEdit, QPushButton, QComboBox, QSlider,
                             QGroupBox, QDial)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 7-12_2022")
        caixaV = QVBoxLayout()
        caixaH = QHBoxLayout()
        # Añadir los movidos de arribaa
        caixaV2 = QVBoxLayout()

        # Añadir los botones del medio
        caixaH2 = QHBoxLayout()

        # Las cosas del final
        caixaH3 = QHBoxLayout()
        caixaV3 = QVBoxLayout()
        caixaV4 = QVBoxLayout()

        self.tedCadroTexto = QTextEdit()
        caixaH.addWidget(self.tedCadroTexto)

        botones1 = QHBoxLayout()

        self.dilVolume = QDial()
        self.dilVolume.setMinimum(0)
        self.dilVolume.setMaximum(8)
        self.dilVolume.valueChanged.connect(self.on_dial_current_indexChanged)

        chkAnimado = QCheckBox("Animado")

        btnSaltar = QPushButton("Saltar")
        cmbSaltar = QComboBox()

        caixaV2.addWidget(self.dilVolume)
        caixaV2.addWidget(chkAnimado)
        botones1.addWidget(btnSaltar)
        botones1.addWidget(cmbSaltar)
        caixaV2.addLayout(botones1)
        caixaV2.addWidget(QWidget())
        caixaH.addLayout(caixaV2)

        self.btnAbrirFich = QPushButton("Abrir ficheiro")
        self.btnReproducir = QPushButton("Reproducir ficheiro")
        self.btnGardar = QPushButton("Gardar")
        self.btnEliminar = QPushButton("Eliminar")

        caixaH2.addWidget(self.btnAbrirFich)
        caixaH2.addWidget(self.btnReproducir)
        caixaH2.addWidget(self.btnGardar)
        caixaH2.addWidget(self.btnEliminar)

        opcionsReproduccion = QGroupBox("Opcións de reproducción")

        self.chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        self.chkFiltrar.stateChanged.connect(self.on_option_current_itemSelected2)
        self.chkEXML = QCheckBox("É XML")
        self.chkEXML.stateChanged.connect(self.on_option_current_itemSelected)
        self.chkRepNPL = QCheckBox("Reproducción NPL")
        self.chkRepNPL.stateChanged.connect(self.on_option_current_itemSelected1)

        grid = QGridLayout()

        grid.addWidget(self.chkFiltrar, 0, 1)
        grid.addWidget(self.chkEXML, 1, 1)
        grid.addWidget(self.chkRepNPL, 2, 1)

        opcionsReproduccion.setLayout(grid)
        caixaH3.addWidget(opcionsReproduccion)

        lblVolume = QLabel("volume:")
        lblFormato = QLabel("Formato:")
        lblSaidaAudio = QLabel("SaidaAudio")
        caixaV4.addWidget(lblVolume)
        caixaV4.addWidget(lblFormato)
        caixaV4.addWidget(lblSaidaAudio)

        caixaH3.addLayout(caixaV4)

        self.sldVolume = QSlider(Qt.Orientation.Horizontal)
        self.sldVolume.setMaximum(8)
        self.sldVolume.setMinimum(0)

        self.cmbFormato = QComboBox()
        self.cmbFormato.addItems(["mp3", "wav", "wma", "ogg"])
        self.cmbFormato.currentIndexChanged.connect(self.on_combo_current_indexChanged)
        self.cmbSaidaAudio = QComboBox()
        self.cmbSaidaAudio.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        self.cmbSaidaAudio.currentIndexChanged.connect(self.on_volumen_current_indexChanged)

        caixaH3.addLayout(caixaV3)

        caixaV3.addWidget(self.sldVolume)
        caixaV3.addWidget(self.cmbFormato)
        caixaV3.addWidget(self.cmbSaidaAudio)

        caixaV.addLayout(caixaH)
        caixaV.addLayout(caixaH2)
        caixaV.addLayout(caixaH3)

        self.contedor = QWidget()
        self.contedor.setLayout(caixaV)

        self.setCentralWidget(self.contedor)
        self.show()

    def on_combo_current_indexChanged(self, indice):
        # print(indice)
        print(self.cmbFormato.itemText(indice) + ' seleccionado')

    def on_dial_current_indexChanged(self):
        if self.dilVolume.isSliderDown():
            print('Volumen: ')
            print(self.dilVolume.sliderPosition())

    def on_volumen_current_indexChanged(self, indice):
        print(indice)
        self.sldVolume.setSliderPosition(indice)

    def on_option_current_itemSelected(self):
        if self.chkEXML.isChecked():
            self.tedCadroTexto.append(self.chkEXML.text())

    def on_option_current_itemSelected1(self):
        if self.chkRepNPL.isChecked():
            self.tedCadroTexto.append(self.chkRepNPL.text())

    def on_option_current_itemSelected2(self):
        if self.chkFiltrar.isChecked():
            self.tedCadroTexto.append(self.chkFiltrar.text())


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()
