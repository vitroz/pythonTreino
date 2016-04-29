###################### PRIMEIRA QUESTAO

# def contaCaracter(string,caracter):

# 	if(caracter != ''):		
# 		listaOcorrencias = []
# 		for i in range(len(string)):
# 			if(string[i] == caracter):
# 				listaOcorrencias.append(i)
# 		if(len(listaOcorrencias) == 0):
# 			return 'Não hoveram ocorrências deste caracter na frase'
# 		return listaOcorrencias
# 	else:
# 		return 'Caracter não Informado'

# historico = []
# for i in range(3):
# 	frase = input('Informe a frase: ');
# 	caracter = input('Informe o caracter: ');
# 	historico.append(frase)
# 	historico.append(caracter)
# 	print(contaCaracter(frase,caracter))

# print('Historico de Entradas seguidas de Caracteres: ' + str(historico))


###################### SEGUNDA QUESTAO


# conta = input('Informe o valor da conta: ')
# pagamento = input('Informe o valor do pagamento: ')

# caixa = [50,20,10,5,2,1]

# troco = float(pagamento) - float(conta)
# contaGrana =[]
# contador = 0
# for nota in caixa:
# 	if(nota <= troco and contador != troco):
# 		while(contador + nota <= troco):
# 			contador += nota
# 			contaGrana.append(nota)

# print(contaGrana)	


###################### TERCEIRA QUESTAO

# def valorPagamento(valorPrestacao,numDiasAtraso):
# 	if(numDiasAtraso == 0):
# 		return valorPrestacao
# 	else:
# 		valorPrestacao += valorPrestacao*0.03 + 0.01*numDiasAtraso
# 		return valorPrestacao

# qtdVezesPrestacoes = 0
# totalPagamento = 0
# relatorio = [];
# while(1):
# 	valorPrestacao = float(input('Informe o valor da prestacao: '))
# 	qtdVezesPrestacoes += 1
# 	if(valorPrestacao != 0):
# 		numDiasAtraso = float(input('Informe o numero de dias em atraso: '))
# 		totalPagamento = totalPagamento + valorPagamento(valorPrestacao,numDiasAtraso)
# 	if(valorPrestacao == 0):
# 		qtdVezesPrestacoes -= 1
# 		print('Valor prestacao = 0, encerrando o programa')
# 		relatorio.append(qtdVezesPrestacoes)
# 		relatorio.append(totalPagamento)
# 		break
# 	print('Valor a ser pago: '+ str(valorPagamento(valorPrestacao,numDiasAtraso)))

# print('Foram pagas '+str(relatorio[0])+' prestacoes hoje, totalizando em: '+ str(relatorio[1]))



