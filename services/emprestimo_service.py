from controllers.emprestimo_controller import EmprestimoController

class EmprestimoService:
    def __init__(self, conn):
        self.emprestimo_controller = EmprestimoController(conn)

    def realizar_emprestimo(self, usuario_id, livro_id, data_emprestimo):
        """
        Realiza o empréstimo de um livro.
        """
        try:
            self.emprestimo_controller.realizar_emprestimo(usuario_id, livro_id, data_emprestimo)
        except ValueError as e:
            raise ValueError(f"Erro ao realizar empréstimo: {str(e)}")

    def devolver_livro(self, emprestimo_id, data_devolucao):
        """
        Devolve um livro emprestado.
        """
        try:
            self.emprestimo_controller.devolver_emprestimo(emprestimo_id, data_devolucao)
        except ValueError as e:
            raise ValueError(f"Erro ao devolver livro: {str(e)}")
