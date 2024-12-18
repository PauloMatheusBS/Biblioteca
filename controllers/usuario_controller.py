from models.usuario import Usuario


class UsuarioController:
    def __init__(self, db_connection):
        self.conn = db_connection  

    def cadastrar_usuario(self, usuario):
        
        senha_hash = usuario.hash_senha()

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Usuarios (nome, email, senha, cpf, admin) 
            VALUES (%s, %s, %s, %s, %s)
        """, (usuario.nome, usuario.email, senha_hash, usuario.cpf, usuario.admin))
        self.conn.commit()
        cursor.close()

    def consultar_usuarios(self, filtro=None):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM Usuarios"
        if filtro:
            query += " WHERE nome LIKE %s OR email LIKE %s"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    def atualizar_usuario(self, usuario_id, campos):
        cursor = self.conn.cursor()
        sets = ", ".join([f"{campo}=%s" for campo in campos.keys()])
        valores = list(campos.values()) + [usuario_id]
        cursor.execute(f"UPDATE Usuarios SET {sets} WHERE id=%s", valores)
        self.conn.commit()
        cursor.close()

    def excluir_usuario(self, usuario_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE id=%s", (usuario_id,))
        self.conn.commit()
        cursor.close()

    def login(self, email, senha):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios WHERE email=%s", (email,))
        usuario = cursor.fetchone()
        cursor.close()

        if not usuario:
            raise ValueError("Email ou senha incorretos.")

        usuario_obj = Usuario.from_dict(usuario)

        
        if not usuario_obj.verificar_senha(senha):
            raise ValueError("Email ou senha incorretos.")

        return usuario_obj  


    def cadastrar_usuario(self, usuario):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO Usuarios (nome, email, senha, cpf, admin) VALUES (%s, %s, %s, %s, %s)", 
                           (usuario.nome, usuario.email, usuario.senha, usuario.cpf, usuario.admin))
            self.conn.commit()
        except mysql.connector.IntegrityError:
            raise ValueError(f"Erro: Email ou CPF já cadastrado.")
        finally:
            cursor.close()

    def usuario_existe(self, email):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario is not None

    def validar_login(self, email, senha):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuarios WHERE email = %s AND senha = %s", (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario is not None

