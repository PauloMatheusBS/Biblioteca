import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from models.usuario import Usuario  
from controllers.usuario_controller import UsuarioController  

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 400, 300)

        self.init_ui()

    def init_ui(self):
        
        self.label_email = QLabel("Email:", self)
        self.label_senha = QLabel("Senha:", self)

       
        self.email_input = QLineEdit(self)
        self.senha_input = QLineEdit(self)
        self.senha_input.setEchoMode(QLineEdit.Password)

        
        self.login_button = QPushButton("Login", self)
        self.cadastrar_button = QPushButton("Cadastrar", self)

        self.login_button.clicked.connect(self.login)
        self.cadastrar_button.clicked.connect(self.cadastrar)

        
        layout = QVBoxLayout()
        layout.addWidget(self.label_email)
        layout.addWidget(self.email_input)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.senha_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.cadastrar_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def login(self):
        email = self.email_input.text()
        senha = self.senha_input.text()

        
        print(f"Usuário {email} tentando logar...")

    def cadastrar(self):
        print("Redirecionar para tela de cadastro")

