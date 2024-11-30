class CadastroLivroView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Livro")
        self.setGeometry(300, 300, 400, 300)

        self.init_ui()

    def init_ui(self):
        
        self.label_titulo = QLabel("Título:", self)
        self.label_autor = QLabel("Autor:", self)
        self.label_isbn = QLabel("ISBN:", self)
        self.label_genero = QLabel("Gênero:", self)

        
        self.titulo_input = QLineEdit(self)
        self.autor_input = QLineEdit(self)
        self.isbn_input = QLineEdit(self)
        self.genero_input = QLineEdit(self)

        
        self.cadastrar_button = QPushButton("Cadastrar", self)
        self.cadastrar_button.clicked.connect(self.cadastrar_livro)

        
        layout = QVBoxLayout()
        layout.addWidget(self.label_titulo)
        layout.addWidget(self.titulo_input)
        layout.addWidget(self.label_autor)
        layout.addWidget(self.autor_input)
        layout.addWidget(self.label_isbn)
        layout.addWidget(self.isbn_input)
        layout.addWidget(self.label_genero)
        layout.addWidget(self.genero_input)
        layout.addWidget(self.cadastrar_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def cadastrar_livro(self):
        titulo = self.titulo_input.text()
        autor = self.autor_input.text()
        isbn = self.isbn_input.text()
        genero = self.genero_input.text()

        
        print(f"Livro '{titulo}' cadastrado com sucesso!")
