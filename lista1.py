#1) Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.

# listaNumeros = []
# print ('Informe os 5 numeros')
# for i in range(5):
# 	listaNumero.append(input('Numero '+ str(i+1) + ':\n'))
# print (listaNumeros) 

#2) Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

# listaNumerosReais = []
# print ('Informe os 10 numeros reais')
# for i in range(10):
# 	listaNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
# listaNumerosReais.reverse()
# print (listaNumerosReais) 

#3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# listaNotas = []
# media = 0
# print ('Informe as 4 notas')
# for i in range(4):
# 	listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))
# 	media += listaNotas[i]
# media = media/4
# print (listaNotas) 
# print (media)


#4) Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.

# listaChar = []
# consoantes = 0
# print ('Informe os caracters')
# for i in range(10):
# 	listaChar.append((input('Caracter  '+ str(i+1) + ':\n')))
# 	char = listaChar[i]
# 	if(char not in ('a','e','i','o','u')):
# 		consoantes += 1
# print(consoantes)

#Imprima as consoantes.
#5) Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números
#pares na listar PAR e os números IMPARES na lista impar. Imprima os três vetores.
#6) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
#de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
#7) Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20
#elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras
#listas.
#8) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
#lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
#média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,
#. . . ).
#9) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
#perguntas são:
#a) "Telefonou para a vítima?"
#b) "Esteve no local do crime?"
#c) "Mora perto da vítima?"
#d) "Devia para a vítima?"
#e) "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
#ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
#contrário, ele será classificado como "Inocente".
#10) Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
#armazenado). Após esta entrada de dados, faça:
#a) Mostre a quantidade de valores que foram lidos;
#b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#d) Calcule e mostre a soma dos valores;
#e) Calcule e mostre a média dos valores;
#f) Calcule e mostre a quantidade de valores acima da média calculada;
#g) Calcule e mostre a quantidade de valores abaixo de sete;
#h) Encerre o programa com uma mensagem;