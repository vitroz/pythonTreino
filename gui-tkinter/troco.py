# Programa Calcula o Troco, retornando sempre a menor quantidade de notas [50,20,10,5,2,1] possivel.


from tkinter import *
import tkinter.messagebox

top = Tk()
frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

L1 = Label(frame, text="Valor da Conta:")
L1.pack()
E1 = Entry(frame, bd =5) # borda
E1.pack()

L2 = Label(frame, text="Valor Pago:")
L2.pack()
E2 = Entry(frame, bd =5) # borda
E2.pack()

def calculaTroco():
	conta = E1.get()
	pagamento = E2.get()

	caixa = [50,20,10,5,2,1]

	troco = float(pagamento) - float(conta)
	contaGrana =[]
	contador = 0
	for nota in caixa:
		if(nota <= troco and contador != troco):
			while(contador + nota <= troco):
				contador += nota
				contaGrana.append(nota)		
	tkinter.messagebox.showinfo("Troco", 'Notas para troco = ' + str(contaGrana))

	

b = Button(top, text="Calcular Troco", command=calculaTroco)
b.pack()


top.mainloop()