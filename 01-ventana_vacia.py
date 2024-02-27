""" 
Este codigo es la base fundamental para la creacion de cualquier aplicacion 
con PyQT6
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):
    
    # Contructor
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 250, 250)  # Establece el tamaño de la ventana
        self.setWindowTitle('HolaMundo')  # Titulo en la ventana
        self.show()  # Permite visualizar la ventana

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())