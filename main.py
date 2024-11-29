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





import tkinter as tk
from tkinter import messagebox
from controllers.usuario_controller import UsuarioController
from controllers.livro_controller import LivroController
from controllers.emprestimo_controller import EmprestimoController
from database.db_connection import DBConnection
from models.usuario import Usuario
from models.livro import Livro
from models.emprestimo import Emprestimo

# Tela de Login
class LoginView:
    def __init__(self, root, controller):
        self.controller = controller
        self.window = tk.Toplevel(root)
        self.window.title("Login")
        self.window.geometry("400x300")

        # Labels e Entradas
        tk.Label(self.window, text="Email:").pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack()

        tk.Label(self.window, text="Senha:").pack()
        self.senha_entry = tk.Entry(self.window, show="*")
        self.senha_entry.pack()

        # Botões de login e cadastro
        tk.Button(self.window, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.window, text="Cadastrar", command=self.abrir_cadastro_usuario).pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        try:
            usuario = self.controller.login(email, senha)
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario.nome}!")
            self.window.destroy()  # Fecha a janela de login após sucesso
            self.abrir_menu_principal(usuario)  # Abre o menu principal após login
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def abrir_cadastro_usuario(self):
        CadastroUsuarioView(self.window, self.controller)

    def abrir_menu_principal(self, usuario):
        MenuPrincipalView(self.window, usuario)

# Tela de Cadastro de Usuário
class CadastroUsuarioView:
    def __init__(self, root, controller):
        self.controller = controller
        self.window = tk.Toplevel(root)
        self.window.title("Cadastro de Usuário")
        self.window.geometry("400x300")

        # Labels e Entradas
        tk.Label(self.window, text="Nome Completo:").pack()
        self.nome_entry = tk.Entry(self.window)
        self.nome_entry.pack()

        tk.Label(self.window, text="Email:").pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack()

        tk.Label(self.window, text="Senha:").pack()
        self.senha_entry = tk.Entry(self.window, show="*")
        self.senha_entry.pack()

        tk.Label(self.window, text="CPF:").pack()
        self.cpf_entry = tk.Entry(self.window)
        self.cpf_entry.pack()

        # Botão para cadastro
        tk.Button(self.window, text="Cadastrar", command=self.cadastrar_usuario).pack(pady=10)

    def cadastrar_usuario(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        cpf = self.cpf_entry.get()

        if not nome or not email or not senha or not cpf:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")
            return

        usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf, admin=False)

        try:
            self.controller.cadastrar_usuario(usuario)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.window.destroy()  # Fecha a janela após o cadastro
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

# Tela de Menu Principal
class MenuPrincipalView:
    def __init__(self, root, usuario):
        self.usuario = usuario
        self.window = tk.Toplevel(root)
        self.window.title("Menu Principal")
        self.window.geometry("400x300")

        tk.Label(self.window, text=f"Bem-vindo, {usuario.nome}!", font=("Arial", 16)).pack(pady=10)

        # Botões para navegar
        tk.Button(self.window, text="Cadastrar Livro", command=self.cadastrar_livro).pack(pady=10)
        tk.Button(self.window, text="Cadastrar Empréstimo", command=self.cadastrar_emprestimo).pack(pady=10)

    def cadastrar_livro(self):
        CadastroLivroView(self.window, self.usuario)

    def cadastrar_emprestimo(self):
        CadastroEmprestimoView(self.window, self.usuario)

# Tela de Cadastro de Livro
class CadastroLivroView:
    def __init__(self, root, usuario):
        self.usuario = usuario
        self.window = tk.Toplevel(root)
        self.window.title("Cadastro de Livro")
        self.window.geometry("400x300")

        # Labels e Entradas
        tk.Label(self.window, text="Título:").pack()
        self.titulo_entry = tk.Entry(self.window)
        self.titulo_entry.pack()

        tk.Label(self.window, text="Autor:").pack()
        self.autor_entry = tk.Entry(self.window)
        self.autor_entry.pack()

        tk.Label(self.window, text="ISBN:").pack()
        self.isbn_entry = tk.Entry(self.window)
        self.isbn_entry.pack()

        tk.Label(self.window, text="Gênero:").pack()
        self.genero_entry = tk.Entry(self.window)
        self.genero_entry.pack()

        # Botão para cadastrar
        tk.Button(self.window, text="Cadastrar Livro", command=self.cadastrar_livro).pack(pady=10)

    def cadastrar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        isbn = self.isbn_entry.get()
        genero = self.genero_entry.get()

        if not titulo or not autor or not isbn or not genero:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")
            return

        livro = Livro(titulo=titulo, autor=autor, isbn=isbn, genero=genero, disponivel=True)

        try:
            LivroController(self.usuario.conn).cadastrar_livro(livro)
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            self.window.destroy()  # Fecha a janela após o cadastro
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

# Tela de Cadastro de Empréstimo
class CadastroEmprestimoView:
    def __init__(self, root, usuario):
        self.usuario = usuario
        self.window = tk.Toplevel(root)
        self.window.title("Cadastro de Empréstimo")
        self.window.geometry("400x300")

        # Labels e Entradas
        tk.Label(self.window, text="ID do Livro:").pack()
        self.livro_id_entry = tk.Entry(self.window)
        self.livro_id_entry.pack()

        tk.Label(self.window, text="Data de Empréstimo:").pack()
        self.data_emprestimo_entry = tk.Entry(self.window)
        self.data_emprestimo_entry.pack()

        # Botão para cadastrar
        tk.Button(self.window, text="Realizar Empréstimo", command=self.realizar_emprestimo).pack(pady=10)

    def realizar_emprestimo(self):
        livro_id = self.livro_id_entry.get()
        data_emprestimo = self.data_emprestimo_entry.get()

        if not livro_id or not data_emprestimo:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos.")
            return

        try:
            EmprestimoController(self.usuario.conn).realizar_emprestimo(self.usuario.id, livro_id, data_emprestimo)
            messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")
            self.window.destroy()  # Fecha a janela após o empréstimo
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

# Iniciando a aplicação
def iniciar_aplicacao():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    conn = DBConnection()  # Crie a conexão com o banco de dados
    usuario_controller = UsuarioController(conn)
    
    LoginView(root, usuario_controller)  # Inicia a tela de login
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()
