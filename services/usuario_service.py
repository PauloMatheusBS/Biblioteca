from controllers.usuario_controller import UsuarioController

class UsuarioService:
    def __init__(self, conn):
        self.usuario_controller = UsuarioController(conn)

    def registrar_usuario(self, nome, email, senha, cpf, admin=False):
        """
        Registra um novo usuário.
        """
        from models.usuario import Usuario
        usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf, admin=admin)
        
        
        if self.usuario_controller.usuario_existe(email):
            raise ValueError("Email já cadastrado.")
        
        
        self.usuario_controller.cadastrar_usuario(usuario)

    def autenticar_usuario(self, email, senha):
        """
        Autentica um usuário com base no email e senha.
        """
        try:
            return self.usuario_controller.login(email, senha)
        except ValueError as e:
            raise ValueError(f"Erro de autenticação: {str(e)}")
