import copy
m1 = [ [1, 1], [2, 2]]

# m2 = m1 #função que faz com que duas matrizes utilizem o mesmo espaço, a mesma lista ????
# m2 = copy.copy(m1) # função que copia uma matriz e deixa duas identidades diferentes, uma identidade m1 e outra m2
# mas neste caso, se modificar a lista m1, a lista m2 não será alterada:
#m1[0] = [0, 0]
# porém, neste outro caso, se modificar o elemento da lista m1, corromperá também o elemento da lista m2:
# m1[0][0] = 0
# para que isso não ocorra, podemos usar a função:
m2 = copy.deepcopy(m1) # função de copia recursiva que duplica a memória da lista inteira e faz com que os objetos m1 e m2 sejam completamente independentes

print(m1)
print(m2)