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

from database.db_connection import DBConnection
from controllers.usuario_controller import UsuarioController
from controllers.livro_controller import LivroController
from controllers.emprestimo_controller import EmprestimoController
from models.usuario import Usuario
from models.livro import Livro
from models.emprestimo import Emprestimo

def main():
    # Conectar ao banco de dados
    db = DBConnection()
    conn = db.get_conn()  # Agora utilizando get_conn()

    if conn:
        usuario_controller = UsuarioController(conn)
        livro_controller = LivroController(conn)
        emprestimo_controller = EmprestimoController(conn)

        # ### Criar um usuário ###
        print("### Criar Usuário ###")
        novo_usuario = Usuario(nome="Maria Oliveira", email="maria.oliveira@email.com", senha="senha123", cpf="12345678901", admin=False)
        try:
            usuario_controller.cadastrar_usuario(novo_usuario)
            print("Usuário 'Maria Oliveira' cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar usuário: {e}")

        # ### Criar um livro ###
        print("\n### Criar Livro ###")
        novo_livro = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", isbn="9780261103573", genero="Fantasia", disponivel=True)
        try:
            livro_controller.cadastrar_livro(novo_livro)
            print("Livro 'O Senhor dos Anéis' cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar livro: {e}")

        # ### Realizar Empréstimo ###
        print("\n### Realizar Empréstimo ###")
        try:
            emprestimo_controller.realizar_emprestimo(usuario_id=1, livro_id=1, data_emprestimo="2024-11-28")
            print("Empréstimo realizado com sucesso!")
        except ValueError as e:
            print(f"Erro ao realizar empréstimo: {e}")

        # ### Consultar Empréstimos ###
        print("\n### Consultar Empréstimos ###")
        emprestimos = emprestimo_controller.consultar_emprestimos(filtro="1")  # Filtro por usuário_id
        for emprestimo in emprestimos:
            print(f"ID: {emprestimo['id']}, Usuario ID: {emprestimo['usuario_id']}, Livro ID: {emprestimo['livro_id']}, Data Empréstimo: {emprestimo['data_emprestimo']}, Data Devolução: {emprestimo['data_devolucao']}")

        # ### Devolver Empréstimo ###
        print("\n### Devolver Empréstimo ###")
        try:
            emprestimo_controller.devolver_emprestimo(emprestimo_id=1, data_devolucao="2024-12-05")
            print("Empréstimo devolvido com sucesso!")
        except ValueError as e:
            print(f"Erro ao devolver empréstimo: {e}")

        db.close()

if __name__ == "__main__":
    main()





