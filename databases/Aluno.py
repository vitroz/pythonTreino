from DBAlunos import DBAlunos

class Alunos(object):
    def __init__(self, idaluno = 0, nome = "", nota = ""):
        self.info = {}
        self.idaluno = idaluno
        self.nome = nome
        self.nota = nota
   
   
    def inserirAluno(self):
        banco = DBAlunos()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into alunos (nome, nota) values ('" + self.nome + "', '" + self.nota + "' )")
            banco.conexao.commit()
            c.close()
            return "Aluno cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do aluno"
   
    def atualizarAluno(self):
        banco = DBAlunos()
        try:
            c = banco.conexao.cursor()
            c.execute("update alunos set nome = '" + self.nome + "', nota = '" + self.nota + "'")
            banco.conexao.commit()
            c.close()
            return "Aluno atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do aluno"
   
    def apagarAluno(self):
        banco = DBAlunos()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from alunos where idAluno = " + self.idaluno + " ")
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
               self.nota = linha[2]
           c.close()
           return "Busca feita com sucesso!"
        except:
           return "Ocorreu um erro na busca do aluno"
