from controllers.usuario_controller import UsuarioController
from models.admin import Administrador

class AdministradorController(UsuarioController):
    def __init__(self, conn):
        super().__init__(conn)

    def cadastrar_administrador(self, administrador):
        """
        Cadastra um administrador no banco de dados.
        """
        if not isinstance(administrador, Administrador):
            raise ValueError("O objeto deve ser uma instância da classe Administrador.")
        
        administrador.admin = True
        super().cadastrar_usuario(administrador)

    def consultar_administradores(self, filtro=None):
        """
        Consulta apenas administradores.
        """
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM Usuarios WHERE admin = TRUE"
        if filtro:
            query += " AND (nome LIKE %s OR email LIKE %s)"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)
        
        administradores = cursor.fetchall()
        cursor.close()
        return administradores

    def excluir_administrador(self, administrador_id):
        """
        Exclui um administrador pelo ID.
        """
        cursor = self.conn.cursor()
        
        
        cursor.execute("SELECT admin FROM Usuarios WHERE id = %s", (administrador_id,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError("Administrador não encontrado.")
        if not result['admin']:
            raise ValueError("O usuário informado não é um administrador.")
        
        
        cursor.execute("DELETE FROM Usuarios WHERE id = %s", (administrador_id,))
        self.conn.commit()
        cursor.close()

    def promover_a_administrador(self, usuario_id):
        """
        Promove um usuário existente a administrador.
        """
        cursor = self.conn.cursor()
        
        
        cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        
        cursor.execute("UPDATE Usuarios SET admin = TRUE WHERE id = %s", (usuario_id,))
        self.conn.commit()
        cursor.close()

    def __str__(self):
        return "AdministradorController: Gerenciamento de administradores."




from models.admin import Administrador
from database.db_connection import DBConnection


conn = DBConnection().get_conn()
admin_controller = AdministradorController(conn)


novo_admin = Administrador(nome="Admin Teste", email="admin@teste.com", senha="1234", cpf="12345678901")
admin_controller.cadastrar_administrador(novo_admin)


for admin in admin_controller.consultar_administradores():
    print(admin)


admin_controller.promover_a_administrador(usuario_id=5)
