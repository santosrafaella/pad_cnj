# Matrizes

# Matrizes baseadas em listas
# Enquanto um array é uma estrutura para armazenar dados de forma linear, já uma matriz é um array bi-dimensional
# Um array bi-dimensional é um array dentro de um array
# Todas as operações feitas em um array podem ser feitas usando listas
# Em uma lista podemos usar elementos variados, como string junto de int e lista
# Em uma matriz cada item pe acessado por 2 índices (x/linha, y/coluna)
# Estrutura para declarar uma matriz:
# Matriz = [ [0, 1, 2], [3, 4, 5] ]
# print(Matriz) #imprime todas as listas da matriz
# print(Matriz[0]) #imprime a lista que está no indice [0]
# print(Matriz[1][1]) #imprime o elemento que está no indice 1 e coluna 1 (linha 1 e coluna 1), no caso o elemento 4
# print(type(Matriz)) #imprime o tipo da matriz, no caso list pois é uma lista
# Função para inserir um item na matriz
# Matriz.append([6, 7, 8])
# Função que insere um item na matriz na posição estipulada, no caso no indice 1, e redireciona o restante dos argumentos para a direita
# Matriz.insert(1, [6, 7, 8])
# Função que atualiza uma linha inteira, faz uma troca na lista e reatribui o valor da lista que estava no indice escolhido
# Matriz[0] = [-3, -2, -1]
# Função que substitui um elemento, um dado
# Matriz[0][2] = -3
# Função que apaga uma linha/lista da matriz
# del(Matriz[1])
# Função que retorna o tamanho da matriz
# print(len(Matriz))
# Função que fatia uma matriz do indice 1 até o indice 5
# Matriz2 = Matriz[1:5]
# Função que fatia uma matriz do indice 2 até o último índice que a matriz tiver
# Matriz2 = Matriz[2:]
# Função que fatia uma matriz do primeriro indice que uma matriz tiver até o indice 1
# Matriz2 = Matriz[:1]
# Cópia de uma matriz
# m1 = [ [1, 1], [2, 2]]
# m2 = m1 #função que faz com que duas matrizes utilizem o mesmo espaço, a mesma lista ????
# é como se a m1 estivesse apontando para uma caixa e m2 estivesse apontando para a mesma caixa e não que m2 é uma cópia de m1
# é como se duas pessoas estivessem apontando para uma caixa de meias, porém as duas não podem pegar a mesma meia
# quando a lista de m1 é modificada, a lista m2 também é modificado
# Import Copy
# Para criar uma cópia superficial, onde a matriz será realmente copiada, usaresmo a função import copy:
# m1 = [ [1, 1], [2, 2]]
# m2 = copy.copy(m1)
# 
#