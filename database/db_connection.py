import mysql.connector

class DBConnection:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "31747294"
        self.database = "biblioteca"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão bem-sucedida ao banco de dados!")
            return self.connection
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco: {err}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão encerrada.")





