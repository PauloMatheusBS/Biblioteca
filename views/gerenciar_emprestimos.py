class CadastroEmprestimoView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Empréstimo")
        self.setGeometry(300, 300, 400, 300)

        self.init_ui()

    def init_ui(self):
        
        self.label_usuario_id = QLabel("ID do Usuário:", self)
        self.label_livro_id = QLabel("ID do Livro:", self)
        self.label_data_emprestimo = QLabel("Data do Empréstimo:", self)

        
        self.usuario_id_input = QLineEdit(self)
        self.livro_id_input = QLineEdit(self)
        self.data_emprestimo_input = QLineEdit(self)

        
        self.cadastrar_button = QPushButton("Cadastrar Empréstimo", self)
        self.cadastrar_button.clicked.connect(self.cadastrar_emprestimo)

        
        layout = QVBoxLayout()
        layout.addWidget(self.label_usuario_id)
        layout.addWidget(self.usuario_id_input)
        layout.addWidget(self.label_livro_id)
        layout.addWidget(self.livro_id_input)
        layout.addWidget(self.label_data_emprestimo)
        layout.addWidget(self.data_emprestimo_input)
        layout.addWidget(self.cadastrar_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def cadastrar_emprestimo(self):
        usuario_id = self.usuario_id_input.text()
        livro_id = self.livro_id_input.text()
        data_emprestimo = self.data_emprestimo_input.text()

        
        print(f"Empréstimo de livro ID {livro_id} para usuário ID {usuario_id} realizado com sucesso!")
