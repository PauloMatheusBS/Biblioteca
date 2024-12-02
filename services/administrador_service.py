from controllers.admin_controller import AdministradorController

class AdministradorService:
    def __init__(self, conn):
        self.admin_controller = AdministradorController(conn)

    def criar_administrador(self, nome, email, senha, cpf):
        """
        Cria um novo administrador.
        """
        from models.admin import Administrador
        admin = Administrador(nome=nome, email=email, senha=senha, cpf=cpf)
        
        # Registra o administrador
        self.admin_controller.cadastrar_administrador(admin)

    def listar_administradores(self):
        """
        Lista todos os administradores cadastrados.
        """
        return self.admin_controller.consultar_administradores()
