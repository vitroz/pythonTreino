from DBAlunos import DBAlunos

class Alunos(object):
    def __init__(self, idaluno = 0, nome = "", nota1 = "",nota2 = "", nota3 = ""):
        self.info = {}
        self.idaluno = idaluno
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3   
   
    def inserirAluno(self):
        banco = DBAlunos()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into alunos (nome, nota1, nota2, nota3) values ('" + self.nome + "', '" + self.nota1 + "' , '"+self.nota2+"', '"+self.nota3+ "' )")
            banco.conexao.commit()
            c.close()
            return "Aluno cadastrado com sucesso!"
        except Exception as e:
            raise e
            return "Ocorreu um erro na inserção do aluno"
   
    def atualizarAluno(self):
        banco = DBAlunos()
        try:
            print(self.idaluno)
            print(self.nome)
            print(self.nota1)
            print(self.nota2)
            print(self.nota3)
            c = banco.conexao.cursor()
            c.execute("update alunos set nome = '" + self.nome + "', nota1 = '" + self.nota1 + "', nota2 = '" + self.nota2 + "', nota3 = '" + self.nota3 + "' where idaluno = " + self.idaluno + " ")
            banco.conexao.commit()
            c.close()
            return "Aluno atualizado com sucesso!"
        except Exception as e:
            raise e
            return "Ocorreu um erro na alteração do aluno"
   
    def apagarAluno(self):
        banco = DBAlunos()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from alunos where idaluno = " + self.idaluno + " ")
            banco.conexao.commit()
            c.close()
            return "Aluno excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do aluno"
   
    def buscarAluno(self, idaluno):
        banco = DBAlunos()
        try:
           c = banco.conexao.cursor()
           c.execute("select * from alunos where idaluno = " + idaluno + "  ")
           for linha in c:
               self.idaluno = linha[0]
               self.nome = linha[1]
               self.nota1 = linha[2]
               self.nota2 = linha[3]
               self.nota3 = linha[4]
           c.close()
           return linha
        except:
           return "Erro"
