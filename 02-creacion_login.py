import sys
from PyQt6.QtWidgets import (
    QApplication,  # Inicializa la aplicacion
    QWidget,  # Inic. la visualizacion de la app
    QLabel,  # Labels
    QLineEdit,  # TextView
    QPushButton,
    QMessageBox, 
    QCheckBox
)
from PyQt6.QtGui import (
    QFont, 
    QPixmap  # Para usar imagenes
)
from registro import RegistrarUsuarioView


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 360, 250)
        self.setWindowTitle('Sistema de login')
        self.generar_formulario() # aun no creada
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        # Etiqueta de Usuario
        user_label = QLabel(self)
        user_label.setText('Usuario:')
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 54)
        # Caja de texto usuario
        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 50)

        # Etiqueta de Password
        pass_label = QLabel(self)
        pass_label.setText('Password:')
        pass_label.setFont(QFont('Arial', 10))
        pass_label.move(20, 86)
        # Caja de texto Password
        self.pass_input = QLineEdit(self)
        self.pass_input.resize(250, 24)
        self.pass_input.move(90, 86)
        self.pass_input.setEchoMode(
            QLineEdit.EchoMode.Password  # Variable estatica de la libreria que 
        )                                # permite convertir un campo a password

        # checkbox para ver la contraseña
        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText('Ver contraseña')
        self.check_view_password.move(90, 110)
        self.check_view_password.toggled.connect(self.mostrar_contra)  # Envia señal

        # Boton Login
        login_button = QPushButton(self)
        login_button.setText('Login')
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.iniciar_mainview)  # Envia la señal
        # Boton Registro
        register_button = QPushButton(self)
        register_button.setText('Registrate')
        register_button.resize(320, 34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.registrar_usuario)  # Envia señal


    def mostrar_contra(self, clicked):
        if clicked:
            self.pass_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.pass_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def iniciar_mainview():
        pass

    def registrar_usuario(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()


# MAIN ACTIVITY
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Login()
    sys.exit(app.exec())