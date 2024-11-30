from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout,
    QPushButton, QCheckBox, QMessageBox
)
from models.livro import Livro
from controllers.livro_controller import LivroController

class TelaCadastroLivro(QWidget):
    def __init__(self, controller: LivroController):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        # Configurando os elementos da tela
        self.setWindowTitle("Cadastro de Livro")
        self.resize(400, 300)

        # Campos de entrada
        self.titulo_label = QLabel("Título:")
        self.titulo_input = QLineEdit()

        self.autor_label = QLabel("Autor:")
        self.autor_input = QLineEdit()

        self.isbn_label = QLabel("ISBN:")
        self.isbn_input = QLineEdit()

        self.genero_label = QLabel("Gênero:")
        self.genero_input = QLineEdit()

        self.disponivel_label = QLabel("Disponível:")
        self.disponivel_checkbox = QCheckBox()
        self.disponivel_checkbox.setChecked(True)

        # Botão de cadastro
        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.clicked.connect(self.cadastrar_livro)

        # Layout da tela
        layout = QVBoxLayout()

        layout.addWidget(self.titulo_label)
        layout.addWidget(self.titulo_input)

        layout.addWidget(self.autor_label)
        layout.addWidget(self.autor_input)

        layout.addWidget(self.isbn_label)
        layout.addWidget(self.isbn_input)

        layout.addWidget(self.genero_label)
        layout.addWidget(self.genero_input)

        layout.addWidget(self.disponivel_label)
        layout.addWidget(self.disponivel_checkbox)

        layout.addWidget(self.btn_cadastrar)

        self.setLayout(layout)

    def cadastrar_livro(self):
        # Obtém os dados do formulário
        titulo = self.titulo_input.text()
        autor = self.autor_input.text()
        isbn = self.isbn_input.text()
        genero = self.genero_input.text()
        disponivel = self.disponivel_checkbox.isChecked()

        # Validação básica
        if not titulo or not autor or not isbn or not genero:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos!")
            return

        # Cria o objeto Livro e cadastra
        livro = Livro(titulo, autor, isbn, genero, disponivel)

        try:
            self.controller.cadastrar_livro(livro)
            QMessageBox.information(self, "Sucesso", "Livro cadastrado com sucesso!")
            self.limpar_formulario()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao cadastrar livro: {e}")

    def limpar_formulario(self):
        """Limpa os campos do formulário após o cadastro."""
        self.titulo_input.clear()
        self.autor_input.clear()
        self.isbn_input.clear()
        self.genero_input.clear()
        self.disponivel_checkbox.setChecked(True)