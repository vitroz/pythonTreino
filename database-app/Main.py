from Aluno import Alunos
from tkinter import *

# EVENTOS BOTOES

def destroyFrame(Frame):
	for widget in Frame.winfo_children(): #Da um Clear no Frame! 
		widget.destroy()

def inserirAluno():
	destroyFrame(topFrame)

	topFrame.title="Inserir"
	bntInserir['state'] = 'disabled'
	bntExcluir['state'] = 'normal'
	bntAlterar['state'] = 'normal'
	btnConfirmar['state'] = 'normal'
	btnConfirmar.pack(pady=10)
	# LABELS

	lblTitulo = Label(topFrame,text="Cadastrar Aluno",font=('Calibri',20))

	lblNome = Label(topFrame,text="Nome:",font=('bold'))
	lblNota1 = Label(topFrame,text="Nota 1:",font=('bold'))
	lblNota2 = Label(topFrame,text="Nota 2:",font=('bold'))
	lblNota3 = Label(topFrame,text="Nota 3:",font=('bold'))

	lblTitulo.grid(row=0,column=1,pady=5)
	lblNome.grid(row=1,pady=5)
	lblNota1.grid(row=2,pady=5)
	lblNota2.grid(row=3,pady=5)
	lblNota3.grid(row=4,pady=5)

	lblFooter = Label(footerFrame)

	#INPUTS

	inpNome = Entry(topFrame,textvariable=nome)
	inpNota1 = Entry(topFrame,textvariable=nota1)
	inpNota2 = Entry(topFrame,textvariable=nota2)
	inpNota3 = Entry(topFrame,textvariable=nota3)

	inpNome.grid(row=1,column=1,pady=5)
	inpNota1.grid(row=2,column=1,pady=5)
	inpNota2.grid(row=3,column=1,pady=5)
	inpNota3.grid(row=4,column=1,pady=5)

def alterarAluno():
	destroyFrame(topFrame)

	topFrame.title="Alterar"
	bntInserir['state'] = 'normal'
	bntExcluir['state'] = 'normal'
	bntAlterar['state'] = 'disabled'
	btnConfirmar['state'] = 'normal'
	btnConfirmar.pack(pady=10)
	# LABELS

	lblTitulo = Label(topFrame,text="Alterar Dados do Aluno",font=('Calibri',20))

	lblIdAluno = Label(topFrame,text="Id Aluno:",font=('bold'))
	lblNome = Label(topFrame,text="Nome:",font=('bold'))
	lblNota1 = Label(topFrame,text="Nota 1:",font=('bold'))
	lblNota2 = Label(topFrame,text="Nota 2:",font=('bold'))
	lblNota3 = Label(topFrame,text="Nota 3:",font=('bold'))

	lblTitulo.grid(row=0,column=1,pady=5)
	lblIdAluno.grid(row=1,pady=5)
	lblNome.grid(row=2,pady=5)
	lblNota1.grid(row=3,pady=5)
	lblNota2.grid(row=4,pady=5)
	lblNota3.grid(row=5,pady=5)

	lblFooter = Label(footerFrame)

	#INPUTS

	inpIdAluno = Entry(topFrame,textvariable=idaluno)
	inpNome = Entry(topFrame,textvariable=nome)
	inpNota1 = Entry(topFrame,textvariable=nota1)
	inpNota2 = Entry(topFrame,textvariable=nota2)
	inpNota3 = Entry(topFrame,textvariable=nota3)

	inpIdAluno.grid(row=1,column=1,pady=5)
	inpNome.grid(row=2,column=1,pady=5)
	inpNota1.grid(row=3,column=1,pady=5)
	inpNota2.grid(row=4,column=1,pady=5)
	inpNota3.grid(row=5,column=1,pady=5)

def excluirAluno():
	destroyFrame(topFrame)

	topFrame.title='Excluir'
	bntInserir['state'] = 'normal'
	bntExcluir['state'] = 'disabled'
	bntAlterar['state'] = 'normal'
	btnConfirmar['state'] = 'normal'
	btnConfirmar.pack(pady=10)
	# LABELS

	lblTitulo = Label(topFrame,text="Excluir Aluno",font=('Calibri',20))

	lblIdAluno = Label(topFrame,text="Id Aluno:",font=('bold'))

	lblTitulo.grid(row=0,column=1,pady=5)
	lblIdAluno.grid(row=1,pady=5)

	lblFooter = Label(footerFrame)

	#INPUTS

	inpIdAluno = Entry(topFrame,textvariable=idaluno)

	inpIdAluno.grid(row=1,column=1,pady=5)

def listarAlunos():
	destroyFrame(topFrame)

	topFrame.title='Listar'
	bntInserir['state'] = 'normal'
	bntExcluir['state'] = 'normal'
	bntAlterar['state'] = 'normal'
	btnConfirmar['state'] = 'disabled'

	ListAlunos = Listbox(topFrame)
	ListAlunos.insert(1,"Python","PHP")
	ListAlunos.pack()

def CRUD():
	print(topFrame.title)
	if(topFrame.title == 'Inserir'):
		aluno = Alunos()
		aluno.nome = nome.get()
		aluno.nota1 = nota1.get()
		aluno.nota2 = nota2.get()
		aluno.nota3 = nota3.get()
		print(aluno.nome)
		print(aluno.nota1)
		print(aluno.nota2)
		print(aluno.nota3)
	elif(topFrame.title == 'Alterar'):
		aluno = Alunos()
		aluno.idaluno = idaluno.get()
		aluno.nome = nome.get()
		aluno.nota1 = nota1.get()
		aluno.nota2 = nota2.get()
		aluno.nota3 = nota3.get()
		print(aluno.idaluno)
		print(aluno.nome)
		print(aluno.nota1)
		print(aluno.nota2)
		print(aluno.nota3)
	elif(topFrame.title == 'Excluir'):
		aluno = Alunos()
		aluno.idaluno = idaluno.get()
		print(aluno.idaluno)

 		# aluno.inserirAluno




#FRAMES
root = Tk()

# VARIAVEIS QUE GUARDAM INPUT ENTRE AS TELAS
idaluno = StringVar()
nome = StringVar()
nota1 = StringVar()
nota2 = StringVar()
nota3 = StringVar()

root.wm_title("Sistema Alunos")
topFrame = Frame(root)
topFrame.pack(side=TOP,pady=20)

middleFrame = Frame(root)
middleFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack()

footerFrame = Frame(root)
footerFrame.pack(side=BOTTOM)

# BOTOES

bntInserir = Button(middleFrame, text='Cadastrar', fg='white', bg='orange',width=10,height=2,command=inserirAluno)
bntAlterar = Button(middleFrame, text='Alterar', fg='white', bg='blue',width=10,height=2,command=alterarAluno)
bntExcluir = Button(middleFrame, text='Excluir', fg='white', bg='red',width=10,height=2,command=excluirAluno)
bntListar = Button(middleFrame, text='Listar',width=10,height=2,command=listarAlunos)
btnConfirmar = Button(bottomFrame, text='Confirmar',fg='white',bg='green',width=10,height=2,command=CRUD)

bntInserir.pack(side=LEFT,padx=10)

bntAlterar.pack(side=LEFT,padx=10)
bntExcluir.pack(side=LEFT,padx=10)
bntListar.pack(side=LEFT,padx=10)

root.mainloop()


