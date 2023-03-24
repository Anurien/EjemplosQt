import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QLabel, QComboBox


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combi en Python")

        self.combo = QComboBox()
        self.combo.addItems(["home", "Muller", "Furro"])
        self.combo.currentIndexChanged.connect(self.on_combo_current_indexChanged)
        self.combo.currentTextChanged.connect(self.on_combo_current_textChanged)
        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.lista = QListWidget()
        self.lista.addItems(["furrox2","otaku","gamer"])
        self.lista.currentItemChanged.connect(self.on_lista_current_indexChanged)
        self.lista.currentTextChanged.connect(self.on_lista_current_textChanged)

        self.caixaV = QVBoxLayout()
        self.caixaV.addWidget(self.combo)
        self.caixaV.addWidget(self.lista)

        self.contedor = QWidget()
        self.contedor.setLayout(self.caixaV)

        self.setCentralWidget(self.contedor)

        self.show()

    def on_combo_current_indexChanged(self, indice):
        print(indice)
        print(self.combo.itemText(indice))

    def on_combo_current_textChanged(self, texto):
        print(texto)

    def on_lista_current_indexChanged(self, indice):
        print(indice.text())

    def on_lista_current_textChanged(self, texto):
        print(texto)



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
