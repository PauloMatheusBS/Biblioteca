# import sys
# import mysql.connector
# from PyQt5.QtWidgets import QApplication
# from views.main_window import MainWindow
# from database.db_connection import DBConnection

# def main():
    
#     db_connection = DBConnection().connect() # Estabelecendo a conexão com o banco de dados

# if __name__ == "__main__":
#     main()


# from database.db_connection import DBConnection
# from controllers.livro_controller import LivroController
# from models.livro import Livro

# def main():
#     db = DBConnection()
#     conn = db.get_conn()  # Conecta diretamente ao banco

#     if conn:
#         controller = LivroController(conn)  # Passa a conexão diretamente para o controller

#         # ### Criar um novo livro ###
#         print("### Criar Livro ###")
#         novo_livro = Livro(
#             titulo="1984",
#             autor="George Orwell",
#             isbn="9780451524935",
#             genero="Distopia",
#             disponivel=True
#         )
#         controller.cadastrar_livro(novo_livro)
#         print("Livro '1984' adicionado com sucesso!")

#         # ### Consultar Livros ###
#         print("\n### Consultar Livros ###")
#         livros = controller.consultar_livros()
#         for livro in livros:
#             print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Disponível: {livro['disponivel']}")

#         # ### Atualizar Livro ###
#         if livros:
#             print("\n### Atualizar Livro ###")
#             livro_id = livros[0]['id']  # Pegar o ID do primeiro livro cadastrado
#             campos_para_atualizar = {
#                 "titulo": "1984 (Edição Revisada)",
#                 "autor": "George Orwell",
#                 "genero": "Distopia"
#             }
#             controller.atualizar_livro(livro_id, campos_para_atualizar)
#             print(f"Livro com ID {livro_id} atualizado com sucesso!")

#         # ### Excluir Livro ###
#         if livros:
#             print("\n### Excluir Livro ###")
#             livro_id = livros[0]['id']  # Pegar o ID do primeiro livro cadastrado
#             controller.excluir_livro(livro_id)
#             print(f"Livro com ID {livro_id} excluído com sucesso!")

#         db.close()

# if __name__ == "__main__":
#     main()


# from database.db_connection import DBConnection
# from controllers.usuario_controller import UsuarioController
# from models.usuario import Usuario

# def main():
#     # Conectar ao banco de dados
#     conn = DBConnection().get_conn()

#     # Teste de Cadastrar Usuário
#     print("### Cadastrar Usuário ###")
#     try:
#         usuario = Usuario(nome="João Silva", email="joao.silva@email.com", senha="senha123", cpf="12345678901", admin=False)
#         usuario_controller = UsuarioController(conn)
#         usuario_controller.cadastrar_usuario(usuario)
#         print("Usuário cadastrado com sucesso!")
#     except Exception as e:
#         print(f"Erro ao cadastrar usuário: {e}")

#     # Teste de Cadastrar Usuário
#     print("### Cadastrar Usuário ###")
#     try:
#         usuario = Usuario(nome="Paulo Matheus", email="paulo.souza@email.com", senha="123", cpf="03103103131", admin=False)
#         usuario_controller = UsuarioController(conn)
#         usuario_controller.cadastrar_usuario(usuario)
#         print("Usuário cadastrado com sucesso!")
#     except Exception as e:
#         print(f"Erro ao cadastrar usuário: {e}")

#     # Teste de Consultar Usuários
#     print("\n### Consultar Usuários ###")
#     try:
#         usuarios = usuario_controller.consultar_usuarios(filtro="João")
#         for u in usuarios:
#             print(f"ID: {u['id']}, Nome: {u['nome']}, Email: {u['email']}, Admin: {u['admin']}")
#     except Exception as e:
#         print(f"Erro ao consultar usuários: {e}")

#     # Teste de Atualizar Usuário
#     print("\n### Atualizar Usuário ###")
#     try:
#         usuario_id = usuarios[0]['id']  # Pegar o ID do primeiro usuário cadastrado
#         usuario_controller.atualizar_usuario(usuario_id, {'nome': 'João Silva Atualizado'})
#         print("Usuário com ID", usuario_id, "atualizado com sucesso!")
#     except Exception as e:
#         print(f"Erro ao atualizar usuário: {e}")

#     # Teste de Excluir Usuário
#     print("\n### Excluir Usuário ###")
#     try:
#         usuario_controller.excluir_usuario(usuario_id)
#         print(f"Usuário com ID {usuario_id} excluído com sucesso!")
#     except Exception as e:
#         print(f"Erro ao excluir usuário: {e}")

#     # Teste de Login de Usuário
#     print("\n### Login de Usuário ###")
#     try:
#         login_usuario = usuario_controller.login("paulo.souza@email.com", "123")
#         print(f"Usuário {login_usuario.nome} autenticado com sucesso!")
#     except ValueError as e:
#         print(f"Erro ao fazer login: {e}")

#     # Fechar conexão com o banco de dados
#     conn.close()
#     print("\nConexão encerrada.")

# if __name__ == "__main__":
#     main()

# from database.db_connection import DBConnection
# from controllers.usuario_controller import UsuarioController
# from controllers.livro_controller import LivroController
# from controllers.emprestimo_controller import EmprestimoController
# from models.usuario import Usuario
# from models.livro import Livro
# from models.emprestimo import Emprestimo

# def main():
#     # Conectar ao banco de dados
#     db = DBConnection()
#     conn = db.get_conn()  # Agora utilizando get_conn()

#     if conn:
#         usuario_controller = UsuarioController(conn)
#         livro_controller = LivroController(conn)
#         emprestimo_controller = EmprestimoController(conn)

#         # ### Criar um usuário ###
#         print("### Criar Usuário ###")
#         novo_usuario = Usuario(nome="Maria Oliveira", email="maria.oliveira@email.com", senha="senha123", cpf="12345678901", admin=False)
#         try:
#             usuario_controller.cadastrar_usuario(novo_usuario)
#             print("Usuário 'Maria Oliveira' cadastrado com sucesso!")
#         except ValueError as e:
#             print(f"Erro ao cadastrar usuário: {e}")

#         # ### Criar um usuário ###
#         print("### Criar Usuário ###")
#         novo_usuario = Usuario(nome="Paulo", email="paulo@email.com", senha="123", cpf="34345678901", admin=False)
#         try:
#             usuario_controller.cadastrar_usuario(novo_usuario)
#             print("Usuário 'Maria Oliveira' cadastrado com sucesso!")
#         except ValueError as e:
#             print(f"Erro ao cadastrar usuário: {e}")

#         # ### Criar um livro ###
#         print("\n### Criar Livro ###")
#         novo_livro = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", isbn="9780261103573", genero="Fantasia", disponivel=True)
#         try:
#             livro_controller.cadastrar_livro(novo_livro)
#             print("Livro 'O Senhor dos Anéis' cadastrado com sucesso!")
#         except ValueError as e:
#             print(f"Erro ao cadastrar livro: {e}")

#         # ### Realizar Empréstimo ###
#         print("\n### Realizar Empréstimo ###")
#         try:
#             emprestimo_controller.realizar_emprestimo(usuario_id=1, livro_id=1, data_emprestimo="2024-11-28")
#             print("Empréstimo realizado com sucesso!")
#         except ValueError as e:
#             print(f"Erro ao realizar empréstimo: {e}")

#         # ### Consultar Empréstimos ###
#         print("\n### Consultar Empréstimos ###")
#         emprestimos = emprestimo_controller.consultar_emprestimos(filtro="1")  # Filtro por usuário_id
#         for emprestimo in emprestimos:
#             print(f"ID: {emprestimo['id']}, Usuario ID: {emprestimo['usuario_id']}, Livro ID: {emprestimo['livro_id']}, Data Empréstimo: {emprestimo['data_emprestimo']}, Data Devolução: {emprestimo['data_devolucao']}")

#         # ### Devolver Empréstimo ###
#         print("\n### Devolver Empréstimo ###")
#         try:
#             emprestimo_controller.devolver_emprestimo(emprestimo_id=1, data_devolucao="2024-12-05")
#             print("Empréstimo devolvido com sucesso!")
#         except ValueError as e:
#             print(f"Erro ao devolver empréstimo: {e}")

#         db.close()

# if __name__ == "__main__":
#     main()


# import sys
# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QLabel,
#     QLineEdit,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
#     QMessageBox,
# )
# from PyQt5.QtCore import Qt


# class CadastroUsuarioView(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Cadastro de Usuário")
#         self.setGeometry(300, 300, 400, 300)
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()
#         self.label_nome = QLabel("Nome Completo:")
#         self.nome_input = QLineEdit()
#         self.label_email = QLabel("Email:")
#         self.email_input = QLineEdit()
#         self.label_senha = QLabel("Senha:")
#         self.senha_input = QLineEdit()
#         self.senha_input.setEchoMode(QLineEdit.Password)
#         self.label_cpf = QLabel("CPF:")
#         self.cpf_input = QLineEdit()
#         self.cadastrar_button = QPushButton("Cadastrar")
#         self.cadastrar_button.clicked.connect(self.cadastrar_usuario)

#         layout.addWidget(self.label_nome)
#         layout.addWidget(self.nome_input)
#         layout.addWidget(self.label_email)
#         layout.addWidget(self.email_input)
#         layout.addWidget(self.label_senha)
#         layout.addWidget(self.senha_input)
#         layout.addWidget(self.label_cpf)
#         layout.addWidget(self.cpf_input)
#         layout.addWidget(self.cadastrar_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def cadastrar_usuario(self):
#         nome = self.nome_input.text()
#         email = self.email_input.text()
#         senha = self.senha_input.text()
#         cpf = self.cpf_input.text()
#         QMessageBox.information(self, "Cadastro", f"Usuário {nome} cadastrado com sucesso!")


# class LoginView(QMainWindow):
#     def __init__(self, on_login_success, abrir_cadastro_usuario):
#         super().__init__()
#         self.setWindowTitle("Login")
#         self.setGeometry(300, 300, 400, 300)
#         self.on_login_success = on_login_success
#         self.abrir_cadastro_usuario = abrir_cadastro_usuario
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()
#         self.label_email = QLabel("Email:")
#         self.email_input = QLineEdit()
#         self.label_senha = QLabel("Senha:")
#         self.senha_input = QLineEdit()
#         self.senha_input.setEchoMode(QLineEdit.Password)

#         # Botões de login e cadastro
#         self.login_button = QPushButton("Login")
#         self.login_button.clicked.connect(self.login)

#         self.cadastrar_button = QPushButton("Cadastrar")
#         self.cadastrar_button.clicked.connect(self.abrir_cadastro_usuario)

#         layout.addWidget(self.label_email)
#         layout.addWidget(self.email_input)
#         layout.addWidget(self.label_senha)
#         layout.addWidget(self.senha_input)
#         layout.addWidget(self.login_button)
#         layout.addWidget(self.cadastrar_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def login(self):
#         email = self.email_input.text()
#         senha = self.senha_input.text()
#         if email == "admin@admin.com" and senha == "admin":  # Validação simples
#             self.on_login_success()
#             self.close()
#         else:
#             QMessageBox.warning(self, "Erro", "Credenciais inválidas!")


# class MenuPrincipal(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Menu Principal")
#         self.setGeometry(300, 300, 400, 300)
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()
#         self.cadastro_usuario_button = QPushButton("Cadastro de Usuário")
#         self.cadastro_usuario_button.clicked.connect(self.abrir_cadastro_usuario)

#         layout.addWidget(self.cadastro_usuario_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def abrir_cadastro_usuario(self):
#         self.cadastro_usuario = CadastroUsuarioView()
#         self.cadastro_usuario.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     def iniciar_menu():
#         menu = MenuPrincipal()
#         menu.show()

#     def abrir_cadastro_usuario():
#         cadastro_usuario = CadastroUsuarioView()  # Instancia a tela de cadastro
#         cadastro_usuario.show()  # Exibe a tela

#     login = LoginView(on_login_success=iniciar_menu, abrir_cadastro_usuario=abrir_cadastro_usuario)
#     login.show()

#     sys.exit(app.exec_())





# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
# from PyQt5.QtGui import QFont
# from models.usuario import Usuario
# from controllers.usuario_controller import UsuarioController
# from database.db_connection import DBConnection

# class TelaCadastroUsuario(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Cadastro de Usuário")
#         self.setGeometry(100, 100, 400, 300)

#         self.initUI()
#         self.controller = UsuarioController(DBConnection().get_conn())

#     def initUI(self):
#         layout = QVBoxLayout()

#         self.label_titulo = QLabel("Cadastro de Usuário")
#         self.label_titulo.setFont(QFont("Arial", 16))
#         layout.addWidget(self.label_titulo)

#         self.input_nome = QLineEdit(self)
#         self.input_nome.setPlaceholderText("Nome")
#         layout.addWidget(self.input_nome)

#         self.input_email = QLineEdit(self)
#         self.input_email.setPlaceholderText("E-mail")
#         layout.addWidget(self.input_email)

#         self.input_senha = QLineEdit(self)
#         self.input_senha.setPlaceholderText("Senha")
#         self.input_senha.setEchoMode(QLineEdit.Password)
#         layout.addWidget(self.input_senha)

#         self.input_cpf = QLineEdit(self)
#         self.input_cpf.setPlaceholderText("CPF (apenas números)")
#         layout.addWidget(self.input_cpf)

#         self.checkbox_admin = QCheckBox("Administrador")
#         layout.addWidget(self.checkbox_admin)

#         self.btn_cadastrar = QPushButton("Cadastrar")
#         self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)
#         layout.addWidget(self.btn_cadastrar)

#         self.setLayout(layout)

#     def cadastrar_usuario(self):
#         nome = self.input_nome.text()
#         email = self.input_email.text()
#         senha = self.input_senha.text()
#         cpf = self.input_cpf.text()
#         admin = self.checkbox_admin.isChecked()

#         if not nome or not email or not senha or not cpf:
#             QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
#             return

#         if not Usuario.validar_email(email):
#             QMessageBox.warning(self, "Erro", "E-mail inválido.")
#             return

#         if not Usuario.validar_cpf(cpf):
#             QMessageBox.warning(self, "Erro", "CPF inválido.")
#             return

#         try:
#             usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf, admin=admin)
#             usuario.senha = usuario.hash_senha().decode()  
#             self.controller.cadastrar_usuario(usuario)
#             QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
#             self.limpar_campos()
#         except ValueError as e:
#             QMessageBox.warning(self, "Erro", str(e))

#     def limpar_campos(self):
#         self.input_nome.clear()
#         self.input_email.clear()
#         self.input_senha.clear()
#         self.input_cpf.clear()
#         self.checkbox_admin.setChecked(False)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = TelaCadastroUsuario()
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication
from views.gerenciar_livros import TelaCadastroLivro
from controllers.livro_controller import LivroController
from database.db_connection import DBConnection

def main():
    # Inicializa a aplicação
    app = QApplication(sys.argv)

    # Configurações do banco de dados
    db = DBConnection()
    conn = db.get_conn()

    # Instancia o controller
    controller = LivroController(conn)

    # Cria e exibe a tela de cadastro
    tela = TelaCadastroLivro(controller)
    tela.show()

    # Executa a aplicação
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


