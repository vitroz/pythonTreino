# Python Lista 2
# Aluno: Vitor Daniel Vieira de Queiroz

# 1) Implementar duas funções:
# Uma que converta temperatura em graus Celsius para Fahrenheit.

# def celsiusfheit(tempCelsius):
# 	fheit = tempCelsius *  1.8 + 32
# 	return fheit

# print(celsiusfheit(32))

# Outra que converta temperatura em graus Fahrenheit para Celsius.

# def fheitCelsius(tempFheit):
# 	celsius = (tempFheit - 32) *  0.55
# 	return int(round(celsius))

# print(fheitCelsius(68))

# 2) Implementar uma função que retorne verdadeiro se o número for primo (falso caso
# contrário). Testar de 1 a 100.

# def primo(numero):
# 	for i in range(2,numero):
# 		if not numero%i:
# 			return False
# 		else:
# 			print(str(numero) + ' eh primo')
# 			return True

# print(primo(10))
# print(primo(13))

# for numero in range(1,101):
# 	primo(numero)

# 3) Implementar uma função que receba uma lista de listas de comprimentos quaisquer e retorne
# uma lista de uma dimensão.

listaListas = [[180.0], [173.8], [164.2], [156.5], [147.2], [138.2]]

#ou

listaDimensao = []
for lista in listaListas:
    for elemento in lista:
        listaDimensao.append(elemento)

print(listaDimensao)

# 4) Escreva uma função que:
# Receba uma frase como parâmetro.
# Retorne uma nova frase com cada palavra com as letras invertidas

# def reverseFrase(frase):
# 	listaFrase = frase.split(" ")
# 	fraseReverse = ''
# 	for palavra in listaFrase:
# 		fraseReverse += palavra[::-1] + ' '
# 	return fraseReverse

# print(reverseFrase('uma frase qualquer'))

