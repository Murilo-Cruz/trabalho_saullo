import sqlite3

class Model:
    def __init__(self, nome_banco_dados):
        self.conn = sqlite3.connect(nome_banco_dados)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS banco_dados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                salario REAL,
                datanascimento TEXT,
                telefone TEXT
            )
        ''')
        self.conn.commit()

    def insert_data(self, nome, salario, datanascimento, telefone):
        print("model",nome)
        self.cursor.execute('''
            INSERT INTO banco_dados (nome, salario, datanascimento, telefone)
            VALUES (?, ?, ?, ?)
        ''', (nome, salario, datanascimento, telefone))
        self.conn.commit()

    def update_data(self, id, nome, salario, datanascimento, telefone):
        self.cursor.execute('''
            UPDATE banco_dados
            SET nome=?, salario=?, datanascimento=?, telefone=?
            WHERE id=?
        ''', (nome, salario, datanascimento, telefone, id))
        self.conn.commit()

    def delete_data(self, id):
        self.cursor.execute('''
            DELETE FROM banco_dados WHERE id=?
        ''', (id,))
        self.conn.commit()

    def get_data(self):
        self.cursor.execute("SELECT * FROM banco_dados")
        return self.cursor.fetchall()
    
    def aumentar_salario(self, id, novo_salario):
        self.cursor.execute('''
            UPDATE banco_dados
            SET salario=?
            WHERE id=?
        ''', (novo_salario, id))
        self.conn.commit()




