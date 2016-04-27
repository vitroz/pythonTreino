class Quadrado:
	def __init__(self, lado):
		self.lado = lado

	def setLado(self,lado):
		self.lado = lado

	def getLado(self):
		return self.lado

	def calculaAreaQuadrado(self):
		return self.lado * self.lado

class Carro:
	def __init__(self,nivelCombustivel,consumoCombustivel):
		self.nivelCombustivel = 0
		self.consumoCombustivel = consumoCombustivel

	def mover(self,km):
		consumo = km/self.consumoCombustivel 
		# consumo em litros
		if(self.nivelCombustivel > 0):
			self.nivelCombustivel = self.nivelCombustivel - consumo
		else:
			print('Carro está no prego, não é possivel se mover')

	def gasolina(self):
		return self.nivelCombustivel

	def abastecerLitros(self,litrosGasolina):
		self.nivelCombustivel += litrosGasolina


quadrado = Quadrado(2)
quadrado.setLado(6)
print('Cada lado do quadrado mede: ' + str(quadrado.getLado()))

print('Área do quadrado igual a: '+ str(quadrado.calculaAreaQuadrado()) + '\n')

honda = Carro(0,12)
print('Este Carro consome: '+str(honda.consumoCombustivel)+' KM/litro')
print('Nivel de combustivel do carro: ' + str(honda.gasolina()))
honda.abastecerLitros(30)
print('Abastecendo carro...')
print('Nivel de combustivel do carro: ' + str(honda.gasolina()))
kmsRodados = 60
print('Dando uma volta de '+str(kmsRodados)+'km com o carro...')
honda.mover(kmsRodados)
print('Nivel de combustivel do carro: ' + str(honda.gasolina()))
