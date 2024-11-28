import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from models.usuario import Usuario  # Importando a model Usuario
from controllers.usuario_controller import UsuarioController  # Controller para interação com o BD

class LoginWindow(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.usuario_controller = UsuarioController(conn)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tela de Login')
        self.setGeometry(100, 100, 300, 200)

        # Layouts
        main_layout = QVBoxLayout()
        form_layout = QVBoxLayout()

        # Campos de entrada
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText('Digite seu e-mail')
        
        self.senha_input = QLineEdit(self)
        self.senha_input.setPlaceholderText('Digite sua senha')
        self.senha_input.setEchoMode(QLineEdit.Password)

        # Botões de login e cadastro
        self.login_button = QPushButton('Logar', self)
        self.login_button.clicked.connect(self.login)

        self.cadastrar_button = QPushButton('Cadastrar', self)
        self.cadastrar_button.clicked.connect(self.cadastrar)

        # Adiciona widgets ao layout
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.senha_input)
        form_layout.addWidget(self.login_button)
        form_layout.addWidget(self.cadastrar_button)

        # Layout principal
        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

    def login(self):
        email = self.email_input.text()
        senha = self.senha_input.text()

        if self.usuario_controller.validar_login(email, senha):
            QMessageBox.information(self, 'Sucesso', 'Login bem-sucedido!')
        else:
            QMessageBox.warning(self, 'Erro', 'Usuário ou senha incorretos!')

    def cadastrar(self):
        email = self.email_input.text()
        senha = self.senha_input.text()

        if self.usuario_controller.usuario_existe(email):
            QMessageBox.warning(self, 'Erro', 'E-mail já cadastrado!')
        else:
            novo_usuario = Usuario(nome="Novo Usuário", email=email, senha=senha, cpf="00000000000", admin=False)
            self.usuario_controller.cadastrar_usuario(novo_usuario)
            QMessageBox.information(self, 'Sucesso', 'Cadastro realizado com sucesso!')

def run_app(conn):
    app = QApplication(sys.argv)
    window = LoginWindow(conn)
    window.show()
    sys.exit(app.exec_())
