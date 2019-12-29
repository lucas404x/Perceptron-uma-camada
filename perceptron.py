import random

class Perceptron:
	def __init__(self, limiar, parada, taxa_aprendizado = 0.1):

		self.pesos = []
		self.limiar = limiar
		self.parada = parada
		self.taxa_aprendizado = taxa_aprendizado

	def treinar(self, dados, classe):
		self.pesos = [[random.random() for j in range(len(dados[0]))] for i in range(len(dados))]
		melhor_acuracia = None
		aux = self.parada

		while 1:
			resultados = []
			u = 0			
			
			for i in range(len(dados)):
				for j in range(len(dados[0])):
					u += dados[i][j] * self.pesos[i][j]

				resultados.append(self.__funcao_ativacao(u))

			acuracia = self.__acuracia(classe, resultados)

			if melhor_acuracia == 1:
				break				
			
			if melhor_acuracia == None or melhor_acuracia < acuracia:
				aux = self.parada
				melhor_acuracia = acuracia

			if melhor_acuracia >= acuracia:
				aux -= 1
				if aux == 0:
					break

			self.__ajustar_pesos(dados, resultados, classe)

	def predicao(self, dados):
		resultados = []

		for i in range(len(dados)):
			u = 0
			for j in range(len(dados[0])):
				u += dados[i][j] * self.pesos[i][j]
			
			resultados.append(self.__funcao_ativacao(u))
		
		return resultados

	def __ajustar_pesos(self, dados, resultados, classe):
		erro = self.__mean_square_error(classe, resultados)

		for i in range(len(self.pesos)):
			for j in range(len(self.pesos[0])):
				self.pesos[i][j] = self.pesos[i][j] + (self.taxa_aprendizado * dados[i][j] * erro)
	
	def __mean_square_error(self, classe, resultados):
		return (1/len(dados)) * sum(list([(classe[i] - resultados[i])**2 for i in range(len(classe))
		if (classe[i] - resultados[i])**2 != 0]))

	def __acuracia(self, resultados, classe):
		acertos = 0
		total_registros = len(classe)

		for i in range(total_registros):
			if classe[i] == resultados[i]:
				acertos += 1

		return acertos/total_registros


	def __funcao_ativacao(self, u):
		return 1 if u > self.limiar else 0


if __name__ == '__main__':

	perceptron = Perceptron(limiar = 1, parada = 1000, taxa_aprendizado = 0.5)
	dados = [[1, 1], [0, 0], [1, 0], [1, 1]]
	classe = [1, 0, 0, 1]
	perceptron.treinar(dados, classe)
	dados_teste = [[random.randint(0, 1) for j in range(len(dados[0]))] for i in range(len(dados))]
	print(dados_teste)
	print(perceptron.predicao(dados_teste))