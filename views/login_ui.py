import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from controllers.usuario_controller import UsuarioController
from database.db_connection import DBConnection
from tela_cadastro_usuario import TelaCadastroUsuario

class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)
        
        # Label e campo para o email
        self.label_email = QLabel("Email:", self)
        self.label_email.setGeometry(50, 50, 100, 30)
        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(150, 50, 200, 30)

        # Label e campo para a senha
        self.label_senha = QLabel("Senha:", self)
        self.label_senha.setGeometry(50, 100, 100, 30)
        self.input_senha = QLineEdit(self)
        self.input_senha.setGeometry(150, 100, 200, 30)
        self.input_senha.setEchoMode(QLineEdit.Password)

        # Botão de login
        self.botao_login = QPushButton("Entrar", self)
        self.botao_login.setGeometry(50, 150, 300, 30)
        self.botao_login.clicked.connect(self.fazer_login)

        # Botão de cadastro
        self.botao_cadastrar = QPushButton("Cadastre-se", self)
        self.botao_cadastrar.setGeometry(50, 200, 300, 30)
        self.botao_cadastrar.clicked.connect(self.abrir_tela_cadastro)

        # Inicializa o controlador de usuários
        db = DBConnection().get_conn()
        self.usuario_controller = UsuarioController(db)

    def fazer_login(self):
        email = self.input_email.text()
        senha = self.input_senha.text()

        try:
            usuario = self.usuario_controller.login(email, senha)
            QMessageBox.information(self, "Login Bem-sucedido", f"Bem-vindo(a), {usuario.nome}!")
        except ValueError as e:
            QMessageBox.warning(self, "Erro no Login", str(e))

    def abrir_tela_cadastro(self):
        self.tela_cadastro = TelaCadastroUsuario()
        self.tela_cadastro.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaLogin()
    tela.show()
    sys.exit(app.exec_())
