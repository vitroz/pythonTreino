def numeroTriangular(i,numero):
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

print(numeroTriangular(1,6))
print(numeroTriangular(1,24))
print(numeroTriangular(1,60))
print(numeroTriangular(1,120))
print(numeroTriangular(1,336))
print(numeroTriangular(1,245))