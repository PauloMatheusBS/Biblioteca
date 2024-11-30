import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController
from database.db_connection import DBConnection

class TelaCadastroUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Usuário")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()
        self.controller = UsuarioController(DBConnection().get_conn())

    def initUI(self):
        layout = QVBoxLayout()

        self.label_titulo = QLabel("Cadastro de Usuário")
        self.label_titulo.setFont(QFont("Arial", 16))
        layout.addWidget(self.label_titulo)

        self.input_nome = QLineEdit(self)
        self.input_nome.setPlaceholderText("Nome")
        layout.addWidget(self.input_nome)

        self.input_email = QLineEdit(self)
        self.input_email.setPlaceholderText("E-mail")
        layout.addWidget(self.input_email)

        self.input_senha = QLineEdit(self)
        self.input_senha.setPlaceholderText("Senha")
        self.input_senha.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_senha)

        self.input_cpf = QLineEdit(self)
        self.input_cpf.setPlaceholderText("CPF (apenas números)")
        layout.addWidget(self.input_cpf)

        self.checkbox_admin = QCheckBox("Administrador")
        layout.addWidget(self.checkbox_admin)

        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)
        layout.addWidget(self.btn_cadastrar)

        self.setLayout(layout)

    def cadastrar_usuario(self):
        nome = self.input_nome.text()
        email = self.input_email.text()
        senha = self.input_senha.text()
        cpf = self.input_cpf.text()
        admin = self.checkbox_admin.isChecked()

        if not nome or not email or not senha or not cpf:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        if not Usuario.validar_email(email):
            QMessageBox.warning(self, "Erro", "E-mail inválido.")
            return

        if not Usuario.validar_cpf(cpf):
            QMessageBox.warning(self, "Erro", "CPF inválido.")
            return

        try:
            usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf, admin=admin)
            usuario.senha = usuario.hash_senha().decode()  
            self.controller.cadastrar_usuario(usuario)
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            self.limpar_campos()
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))

    def limpar_campos(self):
        self.input_nome.clear()
        self.input_email.clear()
        self.input_senha.clear()
        self.input_cpf.clear()
        self.checkbox_admin.setChecked(False)