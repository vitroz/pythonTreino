from Aluno import Alunos
from tkinter import *

class Application:
	def __init__(self, master=None):
		self.fonte = ("Verdana", "8")
		self.container1 = Frame(master)
		self.container1["pady"] = 10
		self.container1.pack()
		self.container2 = Frame(master)
		self.container2["padx"] = 20
		self.container2["pady"] = 5
		self.container2.pack()
		self.container3 = Frame(master)
		self.container3["padx"] = 20
		self.container3["pady"] = 5
		self.container3.pack()
		self.container4 = Frame(master)
		self.container4["padx"] = 20
		self.container4["pady"] = 5
		self.container4.pack()
		self.container6 = Frame(master)
		self.container6["padx"] = 20
		self.container6["pady"] = 5
		self.container6.pack()
		self.container5 = Frame(master)
		self.container5["pady"] = 15
		self.container5.pack()


		self.bntInsert = Button(self.container4, text="Inserir", font=self.fonte, width=12)
		self.bntInsert["command"] = self.inserirAluno
		self.bntInsert.pack (side=LEFT)

		self.bntAlterar = Button(self.container4, text="Alterar", font=self.fonte, width=12)
		self.bntAlterar["command"] = self.alterarAluno
		self.bntAlterar.pack (side=LEFT)

		self.bntExcluir = Button(self.container4, text="Excluir", font=self.fonte, width=12)
		self.bntExcluir["command"] = self.excluirAluno
		self.bntExcluir.pack(side=LEFT)

		self.bntListar = Button(self.container6, text="Listar", font=self.fonte, width=12)
		self.bntListar["command"] = self.listarAluno
		self.bntListar.pack(side=LEFT)

		self.lblmsg = Label(self.container5, text="")
		self.lblmsg["font"] = ("Verdana", "9", "italic")
		self.lblmsg.pack()   


	def inserirAluno(self):
		self.titulo = Label(self.container1, text="Cadastrar Aluno ")
		self.titulo["font"] = ("Calibri", "12", "bold")
		self.titulo.pack ()

		self.lblnome = Label(self.container2, text="Nome:", font=self.fonte, width=10)
		self.lblnome.pack(side=LEFT)

		self.txtnome = Entry(self.container2)
		self.txtnome["width"] = 25
		self.txtnome["font"] = self.fonte
		self.txtnome.pack(side=LEFT)

		self.lblnota = Label(self.container3, text="Nota:", font=self.fonte, width=10)
		self.lblnota.pack(side=LEFT)

		self.txtnota = Entry(self.container3)
		self.txtnota["width"] = 25
		self.txtnota["font"] = self.fonte
		self.txtnota.pack(side=LEFT)

		aluno = Alunos()
		aluno.nome = self.txtnome.get()
		aluno.nota = self.txtnota.get()

		self.lblmsg["text"] = aluno.inserirAluno()

		self.txtidaluno.delete(0, END)
		self.txtnome.delete(0, END)
		self.txtnota.delete(0, END)


	def alterarAluno(self):
		aluno = Alunos()
		aluno.idaluno = self.txtidaluno.get()
		aluno.nome = self.txtnome.get()
		aluno.nota = self.txtnota.get()

		self.lblmsg["text"] = aluno.atualizarAluno()
		self.txtidaluno.delete(0, END)
		self.txtnome.delete(0, END)
		self.txtnota.delete(0, END)	   


	def excluirAluno(self):
		aluno = Alunos()
		aluno.idalunos = self.txtidaluno.get()
		self.lblmsg["text"] = aluno.apagarAluno()
		self.txtidaluno.delete(0, END)
		self.txtnome.delete(0, END)
		self.txtnota.delete(0, END)

	def listarAluno(self):
		aluno = Alunos()
		aluno.idalunos = self.txtidaluno.get()
		self.lblmsg["text"] = user.listarAluno(idaluno)

		self.txtidaluno.delete(0, END)
		self.txtidaluno.insert(INSERT, user.idaluno)

		self.txtnome.delete(0, END)
		self.txtnome.insert(INSERT, user.nome)

		self.txtnota.delete(0, END)
		self.txtnota.insert(INSERT,user.nota)

root = Tk()
Application(root)
root.mainloop()
