from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class CadastroUsuarioView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Usuário")
        self.setGeometry(300, 300, 400, 300)

        self.init_ui()

    def init_ui(self):
        # Labels
        self.label_nome = QLabel("Nome Completo:", self)
        self.label_email = QLabel("Email:", self)
        self.label_senha = QLabel("Senha:", self)
        self.label_cpf = QLabel("CPF:", self)

        # Campos de entrada
        self.nome_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.senha_input = QLineEdit(self)
        self.senha_input.setEchoMode(QLineEdit.Password)  # Ocultar senha
        self.cpf_input = QLineEdit(self)

        # Botões
        self.cadastrar_button = QPushButton("Cadastrar", self)
        self.cadastrar_button.clicked.connect(self.cadastrar_usuario)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_nome)
        layout.addWidget(self.nome_input)
        layout.addWidget(self.label_email)
        layout.addWidget(self.email_input)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.senha_input)
        layout.addWidget(self.label_cpf)
        layout.addWidget(self.cpf_input)
        layout.addWidget(self.cadastrar_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def cadastrar_usuario(self):
        nome = self.nome_input.text()
        email = self.email_input.text()
        senha = self.senha_input.text()
        cpf = self.cpf_input.text()

        # Lógica de cadastro do usuário (verificar e salvar no banco de dados)
        print(f"Usuário {nome} cadastrado com sucesso!")
