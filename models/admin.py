from models.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id=None, nome="", email="", senha="", cpf="", admin=True):
        super().__init__(id=id, nome=nome, email=email, senha=senha, cpf=cpf, admin=admin)

    def acessar_painel_admin(self):
        "aqui ficaria os parametros para criar a tela admin, sei la qundo vai ter isso"
        return "Acesso ao painel administrativo"

    def __str__(self):
        """generico pra por qualuqer coisa"""
        return f"Administrador(nome={self.nome}, email={self.email}, cpf={self.cpf}, admin={self.admin})"




#teste

admin = Administrador(nome="Ademir", email="Ademir@email.com", senha="Ademir123", cpf="12345678901")
print(admin)
print(admin.acessar_painel_admin())
