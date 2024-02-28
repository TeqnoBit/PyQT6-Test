from PyQt6.QtWidgets import (
    # QApplication,
    # QWidget,
    QDialog,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox
)
from PyQt6.QtGui import QFont

class RegistrarUsuarioView(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setModal(True)  # Bloquea el uso de las demas ventanas hasta que se cierre esta
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100, 100, 360, 300)
        self.setWindowTitle('Registro')

        # Usuario
        user_label = QLabel(self)
        user_label.setText('Usuario:')
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 44)
        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 40)

        # Password
        password_label1 = QLabel(self)
        password_label1.setText('Contraseña:')
        password_label1.setFont(QFont('Arial', 10))
        password_label1.move(20, 74)
        self.password_input1 = QLineEdit(self)
        self.password_input1.resize(250, 24)
        self.password_input1.move(90, 70)
        self.password_input1.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        # Repite Password
        password_label2 = QLabel(self)
        password_label2.setText('Repite:')
        password_label2.setFont(QFont('Arial', 10))
        password_label2.move(20, 104)
        self.password_input2 = QLineEdit(self)
        self.password_input2.resize(250, 24)
        self.password_input2.move(90, 100)
        self.password_input2.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        # Botones
        create_button = QPushButton(self)
        create_button.setText('Crear')
        create_button.resize(150, 32)
        create_button.move(20, 170)
        create_button.clicked.connect(self.crear_usuario)

        cancel_button = QPushButton(self)
        cancel_button.setText('Cancelar')
        cancel_button.resize(150, 32)
        cancel_button.move(170, 170)
        cancel_button.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        self.close()

    def crear_usuario(self):
        # Pasos para registrar usuarios
        user_path = 'usuarios.txt'
        usuario = self.user_input.text()
        password1 = self.password_input1.text()
        password2 = self.password_input2.text()

        if password1 == '' or password2 == '' or usuario == '':
            QMessageBox.warning(
                self, 
                'Error', 
                'No dejar campos vacios',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close
            )
        elif password1 != password2:
            QMessageBox.warning(
                self,                              # Parent
                'Error',                           # Titulo
                'La contraseña no coincide',       # Texto
                QMessageBox.StandardButton.Close,  # Boton
                QMessageBox.StandardButton.Close   # Boton Preseleccionado
            )
        else:
            try:
                # Solo para este ejemplo se usara esta manera de almacenar datos
                with open(user_path, 'a+') as f:
                    f.write(f'{usuario},{password1}\n')
                QMessageBox.information(
                    self,
                    'Creacion Exitosa',
                    'Usuario creado correctamente',
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok
                )
                self.close()
            except FileNotFoundError as e:
                QMessageBox.warning(
                self,                               # parent
                'Error',                            # Titulo de la ventaja
                f'La base de datos no existe: {e}', # Mensaje
                QMessageBox.StandardButton.Close,   # Tipo de boton
                QMessageBox.StandardButton.Close    # Preselecciona
            )