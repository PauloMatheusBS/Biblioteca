from database.db_connection import DBConnection
from models.livro import Livro

class LivroController:
    def __init__(self, conn):
        # Agora a conexão é passada diretamente para o controller
        self.conn = conn

    def cadastrar_livro(self, livro):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Livros WHERE isbn = %s", (livro.isbn,))
        if cursor.fetchone()[0] > 0:
            print("Erro: ISBN já cadastrado!")
            return
        cursor.execute("""
            INSERT INTO Livros (titulo, autor, isbn, genero, disponivel) 
            VALUES (%s, %s, %s, %s, %s)
        """, (livro.titulo, livro.autor, livro.isbn, livro.genero, livro.disponivel))
        self.conn.commit()
        cursor.close()

    def consultar_livros(self, filtro=None):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM Livros"
        if filtro:
            query += " WHERE titulo LIKE %s OR autor LIKE %s OR isbn LIKE %s OR genero LIKE %s"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)
        livros = cursor.fetchall()
        cursor.close()
        return livros
    
    def atualizar_livro(self, livro_id, campos):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Livros WHERE id = %s", (livro_id,))
        if cursor.fetchone()[0] == 0:
            print("Erro: Livro não encontrado!")
            return

        if "isbn" in campos:
            print("Erro: Não é permitido alterar o ISBN!")
            return

        sets = ", ".join([f"{campo}=%s" for campo in campos.keys()])
        valores = list(campos.values()) + [livro_id]
        cursor.execute(f"UPDATE Livros SET {sets} WHERE id=%s", valores)
        self.conn.commit()
        cursor.close()

    def excluir_livro(self, livro_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Emprestimos WHERE livro_id = %s AND data_devolucao IS NULL", (livro_id,))
        if cursor.fetchone()[0] > 0:
            print("Erro: O livro está emprestado e não pode ser excluído.")
            return
        cursor.execute("DELETE FROM Livros WHERE id=%s", (livro_id,))
        self.conn.commit()
        cursor.close()




