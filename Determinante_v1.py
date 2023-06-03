#-------------------------------------------------------------------------
#!/usr/bin/env python3 "my_path/Determinante_v1.py"
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------
#Programa: Determinante_v1.py
#Autor: Gabriel Machado Silva Vida
#Github: https://github.com/axelife2021
#E-mail: gabrielmsv732@gmail.com
#-------------------------------------------------------------------------
#Descrição: 

#Programa escrito em Python que calcula e imprime o valor do determinante
#de uma matriz quadrada de ordem maior ou igual a 1.
#-------------------------------------------------------------------------

def calcularDetCompl(complementar, novaOrdem):
	"""
	Retorna o determinante da matriz complementar dada.
	"""
	if (novaOrdem == 3):
		return regraDeSarrus(complementar)
	else: #Se a complementar for de ordem maior que 3
		return Laplace(complementar, novaOrdem)

def cofator(indices, matriz, ordem, filaDet):
	"""
	Retorna uma lista com os cofatores de cada elemento
	da fila dada.
	"""
	cofatores = []
	cont = 0 #Indica o índice do elemento da fila a ser analisado
	for l, c in indices: #Obtendo os índices de cada elemento da fila
		if (filaDet[cont] == 0):
			cofatores.append(0) #(foi utilizado esse artifício para evitar problemas com indexação na função de calcularDetCompl)
		else: # Se o elemento é diferente de zero
			matrizComplementar = encontrarComplementar(l, c, matriz, ordem)
			detComplementar = calcularDetCompl(matrizComplementar, ordem - 1)
			cofatores.append(((-1) ** (l+c)) * detComplementar)
		cont += 1 #Seguindo para o próximo elemento da fila
	return cofatores

def encontrarComplementar(l, c, matriz, ordem):
    """
	Retorna a matriz complementar de um elemento
	"""
    elemComplementar = []
    for linha in range(len(matriz)): #Percorrendo as linhas da matriz original
        if linha == l:
            pass
        else: #Se não for a linha do elemento em questão
            for coluna in range(len(matriz)): #Percorrendo as colunas da matriz original
                if coluna == c:
                    pass
                else: #Se não for a coluna do elemento em questão
                    elemComplementar.append(matriz[linha][coluna])
	#Dividindo a lista de elementos do complementar e retornando a matriz obtida
    return [elemComplementar[i:i + (ordem -1)] for i in range(0, len(elemComplementar), ordem - 1)]

def coletarIndicesFila(ordem, indiceLinha, indiceColuna,tipoDeFila):
	"""
	Retorna uma lista de tuplas com os índices de cada elemento
	da fila dada.
	""" 
	if (tipoDeFila == "linha"):
		return [(indiceLinha, i) for i in range(ordem)]
	else: #Se a fila é do tipo "coluna"
		return [(i, indiceColuna) for i in range(ordem)]

def contarZerosLinha(matriz):
	"""
	Retorna a linha da matriz com mais zeros e seu índice (contando
	a partir de zero).
	"""
	linhaComMaisZeros = 0
	for m, linha in enumerate(matriz, 0): #Percorrando linhas da matriz
		if (linha.count(0) > matriz[linhaComMaisZeros].count(0)):
			linhaComMaisZeros = m
		else: #Se a linha tomada como a com mais zeros continua sendo a com mais zeros
			linhaComMaisZeros = linhaComMaisZeros
	return matriz[linhaComMaisZeros], linhaComMaisZeros

def contarZerosColuna(matriz, ordem):
    """
    Retorna a coluna com mais zeros da matriz dada e seu índice (contando
	a partir de zero).
	"""
    indiceColunaMaisZeros = 0
    numeroDeZerosMaior = 0
    for c in range(ordem): #Percorrando as colunas da matriz
        numeroDeZerosAtual = 0
        for l in range(ordem): #Percorrendo os elementos da coluna
            if matriz[l][c] == 0:
                numeroDeZerosAtual += 1
            else: #Se o elemento analisado não é zero
                pass
        if (numeroDeZerosAtual > numeroDeZerosMaior):
            indiceColunaMaisZeros = c
            numeroDeZerosMaior = numeroDeZerosAtual
    return [matriz[l][indiceColunaMaisZeros] for l in range(ordem)], indiceColunaMaisZeros
    
def filaComMaisZeros(linha, coluna):
	"""
	Retorna a fila com mais zeros da matriz e o tipo dela.
	"""
	if linha.count(0) >= coluna.count(0):
		return linha, "linha"
	else: # Se a coluna tem mais zeros
		return coluna, "coluna"

def det2por2(matriz):
	"""
	Retorna o valor do determinante de uma matriz 2x2.
	"""
	return matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1]

def regraDeSarrus(matriz):
	"""
	Retorna o valor do determinante de uma matriz 3x3 utilizando a Regra de Sarrus.
	"""
	#Elementos da linha 1
	d11 = matriz[0][0]
	d12 = matriz[0][1]
	d13 = matriz[0][2]
	#Elementos da Linha 2
	d21 = matriz[1][0]
	d22 = matriz[1][1]
	d23 = matriz[1][2]
	#Elementos da Linha 3
	d31 = matriz[2][0]
	d32 = matriz[2][1]
	d33 = matriz[2][2]
	#Somatório dos produtos dos elementos das diagonais principais
	dp = (d11*d22*d33 + d21*d32*d13 + d12*d23*d31)
	#Somatório dos produtos dos elementos das diagonais secundárias
	ds = (d13*d22*d31 + d23*d32*d11 + d12*d21*d33)
	return dp - ds

def Laplace(matriz, ordem):
	"""
	Retorna o valor do determinante de uma matriz de ordem maior que 3 usando o Teorema de Laplace.
	"""
	#Encontrando a linha com mais zeros e seu índice
	linhaComMaisZeros, indiceLinha = contarZerosLinha(matriz)
	
	#Encontrando a coluna com mais zeros e seu índice
	colunaComMaisZeros, indiceColuna = contarZerosColuna(matriz, ordem)
	
	#Definindo qual das duas filas encontradas será usada no Teorema (a com mais zeros)
	filaDet, tipoDeFila = filaComMaisZeros(linhaComMaisZeros, colunaComMaisZeros)
	
	#Armazenando os índices da fila a ser usada
	indices = coletarIndicesFila(ordem, indiceLinha, indiceColuna, tipoDeFila)
	
	#Calculando os cofatores dos elementos da fila
	cofatores = cofator(indices, matriz, ordem, filaDet)

	#Calculando o determinante da matriz
	determinante = 0
	for elemento, cofatorElem in zip(filaDet, cofatores):
		determinante += (elemento*cofatorElem)

	return determinante

def recebeMatriz(ordem):
	"""
	Recebe as linhas da matriz digitadas pelo usuário e retorna-as em uma lista de listas.
	"""
	matriz = []
	for m in range(1, ordem+1):
		#Entrada da linha
		linha = [int(num) for num in input(f"Digite a linha {m}: ").split()]
		matriz.append(linha)
	return matriz

def main():
	#Entrada da ordem da matriz
	ordem = int(input("Digite a ordem da matriz: "))
	
	#Entrada da matriz quadrada
	matriz = recebeMatriz(ordem)

	if (ordem == 1):
		determinante = matriz[0][0]

	elif (ordem == 2):
		determinante = det2por2(matriz)

	elif (ordem == 3):
		determinante = regraDeSarrus(matriz)

	else: #Se a matriz é de ordem maior que 3
		determinante = Laplace(matriz, ordem)
	
	#Imprimindo o valor do determinante
	print(f"O determinante da matriz vale {determinante}")

	return None

if __name__ == "__main__":
	main()