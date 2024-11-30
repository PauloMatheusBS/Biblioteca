from datetime import datetime

class Emprestimo:
    def __init__(self, id=None, usuario_id=None, livro_id=None, data_emprestimo=None, data_devolucao=None):
        self.id = id  
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        
        self.data_emprestimo = datetime.strptime(data_emprestimo, "%Y-%m-%d") if data_emprestimo else None
        self.data_devolucao = datetime.strptime(data_devolucao, "%Y-%m-%d") if data_devolucao else None

    def to_dict(self):
        """Converte o objeto Emprestimo em um dicionário."""
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "livro_id": self.livro_id,
            "data_emprestimo": self.data_emprestimo.strftime("%Y-%m-%d") if self.data_emprestimo else None,
            "data_devolucao": self.data_devolucao.strftime("%Y-%m-%d") if self.data_devolucao else None,
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Emprestimo a partir de um dicionário."""
        return Emprestimo(
            id=data.get("id"),
            usuario_id=data.get("usuario_id"),
            livro_id=data.get("livro_id"),
            data_emprestimo=data.get("data_emprestimo"),
            data_devolucao=data.get("data_devolucao"),
        )

    def emprestimo_ativo(self):
        """Verifica se o empréstimo está ativo (sem data de devolução)."""
        return self.data_devolucao is None

    def atualizar_data_devolucao(self, data_devolucao):
        """Atualiza a data de devolução do empréstimo."""
        self.data_devolucao = datetime.strptime(data_devolucao, "%Y-%m-%d")
