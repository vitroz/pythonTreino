# Python Lista 3
# Aluno: Vitor Daniel Vieira de Queiroz

# 1) Implementar um programa que receba um nome de arquivo e gere estatísticas sobre o
# arquivo (número de caracteres, número de linhas e número de palavras)

# caracters = palavras = linhas = 0
# listaPalavras = []
# with open('arquivo.txt', 'r') as arquivo:
# 	for linha in arquivo:
# 		linhas += 1
# 		listaPalavras.append(linha.split())

# for palavra in listaPalavras:
# 	for caracter in palavra:
# 		caracters += len(caracter)

# print('Numero de Caracters: ' + str(caracters))
# print('Numero de Linhas: ' + str(linhas))
# print('Numero de Palavras: ' + str(len(listaPalavras)))


# 2) Faça um script que:
# ▪ Leia um arquivo texto.
# ▪ Conte as ocorrências de cada palavra.
# ▪ Mostre os resultados ordenados pelo número de ocorrências


# listaPalavras = []
# with open('arquivo.txt', 'r') as arquivo:
# 	for linha in arquivo:
# 		listaPalavras.append(linha.split())

# palavras = []
# for lista in listaPalavras:
#     for elemento in lista:
#         palavras.append(elemento)

# ocorrencias = {}
# for palavra in palavras:
# 	ocorrencias.update({palavra : palavras.count(palavra)})

# print(palavras)
# print(ocorrencias)

# ocorrenciasOrdenadas = sorted(ocorrencias.items(), key = lambda t:t[1]) #Ordendo por Valores
# print('Lista de Ocorrencias ordenadas: ' + str(ocorrenciasOrdenadas))

# 3) Terceira Questao
def hbytes(num): # Funcao que converte bytes para MBytes
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%1.3f %s" % (num, x)
        num /= 1024.0
    return "%1.3f %s " % (num, 'TB')

def pctDeUso(usuario,total):
	usuario.append(float(usuario[2])/(total))
	usuario.append("{:.2%}".format(usuario[4]))##indice[4] é a posicao que guarda a porcentagem de espaço consumida.

listaUsuarios = []
cont = total =  pct = 0
with open('usuarios.txt', 'r') as arquivo:
	for linha in arquivo:
		listaUsuarios.append(linha.split()) # Joga em uma lista, uma lista com os usuarios, separados por nome e espaço consumido

	for usuario in listaUsuarios:
		cont += 1
		usuario.insert(0,cont) #inserir no começo da lista
		usuario.append(hbytes(int(usuario[2]))) ##indice[2] é a posicao que guarda o espaco consumido 
		total += int(usuario[2])

	for usuario in listaUsuarios:
		pctDeUso(usuario,total) #Preciso do valor total antes de calcular a media.

numTotal = hbytes(total).split(' ')
media = float(numTotal[0])/cont*1000

with open('relatorio.txt', 'w') as relatorio:
	relatorio.write('ACME Inc.                                             Uso do Espaço em disco pelos usuários\n')
	relatorio.write('----------------------------------------------------------------------------------\n')
	relatorio.write('Nr. Usuario                  Espaço Utilizado            % do uso\n')
	for usuario in listaUsuarios:
		relatorio.write(str(usuario[0]) + '            ' + usuario[1] + '       ' +str(usuario[3])+ '                  ' + str(usuario[5]) + '\n')

	relatorio.write('\n\nEspaço Total Ocupado: ' + hbytes(total))
	relatorio.write('\n\nEspaço médio Ocupado: ' + str(media) + ' MB')
	relatorio.close()





