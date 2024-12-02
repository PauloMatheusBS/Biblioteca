from controllers.livro_controller import LivroController

class LivroService:
    def __init__(self, conn):
        self.livro_controller = LivroController(conn)

    def cadastrar_livro(self, titulo, autor, isbn, genero):
        """
        Cadastra um novo livro, verificando se o ISBN já existe.
        """
        from models.livro import Livro
        livro = Livro(titulo=titulo, autor=autor, isbn=isbn, genero=genero)
        
       
        try:
            self.livro_controller.cadastrar_livro(livro)
        except ValueError as e:
            raise ValueError(f"Erro ao cadastrar livro: {str(e)}")

    def buscar_livros(self, filtro=None):
        """
        Busca livros pelo filtro.
        """
        return self.livro_controller.consultar_livros(filtro=filtro)
