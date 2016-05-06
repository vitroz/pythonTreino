def numeroTriangular(i,numero):
	if(numero > 0):
		while(i <= numero):
			i2 = i+1
			i3 = i+2
			resultado = i *i2 *i3
			i = i + 1
			if(resultado == numero):
				return ('Numero '+str(numero)+' é triangular. Resultado de: '+ str(i-1)+'*'+str(i2)+'*'+str(i3))
			if(resultado > numero): # Evitar iterações adicionais
				break
		return 'Numero '+str(numero)+' não é triangular'
	else:
		return 'Numero Negativo Invalido'

print(numeroTriangular(1,6))
print(numeroTriangular(1,24))
print(numeroTriangular(1,60))
print(numeroTriangular(1,120))
print(numeroTriangular(1,336))
print(numeroTriangular(1,245))
print(numeroTriangular(1,-10))

def numeroPrimo(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

print(numeroPrimo(2))
print(numeroPrimo(71))
print(numeroPrimo(40))

def fatoracao(n):
	divisores = []
	d = 2
	while n > 1: 
		if n%d == 0:
			n = n/d
			divisores.append(d)
		else:
			d += 1

	print(divisores)

fatoracao(630)

def inverteNumero(n):
	return int(str(n)[::-1])

print(inverteNumero(1234))
