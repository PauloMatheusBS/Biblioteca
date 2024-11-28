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
#     conn = db.connect()  # Conecta diretamente ao banco

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

