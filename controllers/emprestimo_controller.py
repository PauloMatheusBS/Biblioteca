from models.emprestimo import Emprestimo
from models.livro import Livro
from models.usuario import Usuario

class EmprestimoController:
    def __init__(self, conn):
        self.conn = conn

    def realizar_emprestimo(self, usuario_id, livro_id, data_emprestimo):
        cursor = self.conn.cursor(dictionary=True)
        
       
        cursor.execute("SELECT * FROM Livros WHERE id = %s", (livro_id,))
        livro = cursor.fetchone()
        
        if not livro or not livro['disponivel']:
            raise ValueError("Livro não disponível para empréstimo.")
        
        
        cursor.execute("SELECT COUNT(*) FROM Emprestimos WHERE usuario_id = %s AND data_devolucao IS NULL", (usuario_id,))
        count = cursor.fetchone()['COUNT(*)']
        
        if count >= 3:
            raise ValueError("Usuário já tem 3 livros emprestados.")
        
        
        cursor.execute("""
            INSERT INTO Emprestimos (usuario_id, livro_id, data_emprestimo, data_devolucao)
            VALUES (%s, %s, %s, NULL)
        """, (usuario_id, livro_id, data_emprestimo))
        self.conn.commit()

        
        cursor.execute("UPDATE Livros SET disponivel = FALSE WHERE id = %s", (livro_id,))
        self.conn.commit()

        cursor.close()

    def devolver_emprestimo(self, emprestimo_id, data_devolucao):
        cursor = self.conn.cursor(dictionary=True)
        
        
        cursor.execute("SELECT * FROM Emprestimos WHERE id = %s AND data_devolucao IS NULL", (emprestimo_id,))
        emprestimo = cursor.fetchone()
        
        if not emprestimo:
            raise ValueError("Empréstimo não encontrado ou já foi devolvido.")
        
        
        cursor.execute("""
            UPDATE Emprestimos
            SET data_devolucao = %s
            WHERE id = %s
        """, (data_devolucao, emprestimo_id))
        
        
        cursor.execute("""
            UPDATE Livros
            SET disponivel = TRUE
            WHERE id = %s
        """, (emprestimo['livro_id'],))
        
        self.conn.commit()
        cursor.close()
        print(f"Empréstimo com ID {emprestimo_id} devolvido com sucesso!")

    def consultar_emprestimos(self, filtro=None):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM Emprestimos"
        
        if filtro:
            query += " WHERE usuario_id LIKE %s OR livro_id LIKE %s"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)
        
        emprestimos = cursor.fetchall()
        cursor.close()
        return emprestimos
