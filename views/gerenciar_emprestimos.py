from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QDateEdit, QWidget, QMessageBox
)
from PyQt5.QtCore import QDate
import sys

from controllers.emprestimo_controller import EmprestimoController
from controllers.livro_controller import LivroController
from controllers.usuario_controller import UsuarioController
from database.db_connection import DBConnection


class EmprestimoWindow(QMainWindow):
    def __init__(self, emprestimo_controller, usuario_controller, livro_controller):
        super().__init__()

        self.emprestimo_controller = emprestimo_controller
        self.usuario_controller = usuario_controller
        self.livro_controller = livro_controller

        self.setWindowTitle("Cadastro de Empréstimo")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        #
        user_layout = QHBoxLayout()
        user_label = QLabel("Usuário:")
        self.user_combo = QComboBox()
        self.populate_users()
        user_layout.addWidget(user_label)
        user_layout.addWidget(self.user_combo)
        layout.addLayout(user_layout)

       
        book_layout = QHBoxLayout()
        book_label = QLabel("Livro:")
        self.book_combo = QComboBox()
        self.populate_books()
        book_layout.addWidget(book_label)
        book_layout.addWidget(self.book_combo)
        layout.addLayout(book_layout)

        
        date_layout = QHBoxLayout()
        date_label = QLabel("Data de Empréstimo:")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        date_layout.addWidget(date_label)
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)

        
        self.save_button = QPushButton("Salvar Empréstimo")
        self.save_button.clicked.connect(self.save_emprestimo)
        layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populate_users(self):
        """Popula o combobox com os usuários disponíveis."""
        self.user_combo.clear()
        try:
            users = self.usuario_controller.consultar_usuarios()
            for user in users:
                self.user_combo.addItem(f"{user['nome']} (ID: {user['id']})", user['id'])
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar usuários: {str(e)}")

    def populate_books(self):
        """Popula o combobox com os livros disponíveis."""
        self.book_combo.clear()
        try:
            books = self.livro_controller.consultar_livros(filtro=None)
            for book in books:
                if book['disponivel']:
                    self.book_combo.addItem(f"{book['titulo']} (ID: {book['id']})", book['id'])
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar livros: {str(e)}")

    def save_emprestimo(self):
        """Salva o empréstimo no banco de dados."""
        user_id = self.user_combo.currentData()
        book_id = self.book_combo.currentData()
        date_emprestimo = self.date_edit.date().toString("yyyy-MM-dd")

        try:
            self.emprestimo_controller.realizar_emprestimo(user_id, book_id, date_emprestimo)
            QMessageBox.information(self, "Sucesso", "Empréstimo realizado com sucesso!")
            self.populate_books()  
        except ValueError as e:
            QMessageBox.warning(self, "Aviso", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar empréstimo: {str(e)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    
    db_connection = DBConnection().get_conn()
    emprestimo_controller = EmprestimoController(db_connection)
    usuario_controller = UsuarioController(db_connection)
    livro_controller = LivroController(db_connection)

    window = EmprestimoWindow(emprestimo_controller, usuario_controller, livro_controller)
    window.show()
    sys.exit(app.exec_())