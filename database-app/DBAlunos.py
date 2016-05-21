import sqlite3
class DBAlunos():
    def __init__(self):
        self.conexao = sqlite3.connect('dbalunos.db')
        self.createTable()
   
    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists alunos (
                  idaluno integer primary key autoincrement ,
                  nome text,
                  nota1 text,
                  nota2 text,
                  nota3 text)""")
        self.conexao.commit()
        c.close()
