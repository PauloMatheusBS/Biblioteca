import mysql.connector

# class DBConnection:
#     def __init__(self):
#         self.host = "127.0.0.1"
#         self.user = "root"
#         self.password = "31747294"
#         self.database = "biblioteca"
#         self.connection = None

#     def connect(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.database
#             )
#             print("Conexão bem-sucedida ao banco de dados!")
#             return self.connection
#         except mysql.connector.Error as err:
#             print(f"Erro ao conectar ao banco: {err}")
#             return None

#     def close(self):
#         if self.connection:
#             self.connection.close()
#             print("Conexão encerrada.")





class DBConnection:
    def __init__(self):
        
        self.config = {
            'host': "127.0.0.1",  
            'user': "root",       
            'password': "31747294",       
            'database': "biblioteca"  
        }
        self.conn = None

    def get_conn(self):
        """Retorna uma conexão com o banco de dados MySQL"""
        if self.conn is None or not self.conn.is_connected():
            self.conn = mysql.connector.connect(**self.config)
        return self.conn

    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn and self.conn.is_connected():
            self.conn.close()







