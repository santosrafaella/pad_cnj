#indices e contagens

#lista_compras = ["maçãs", "leite", "arroz", "frango", "leite", "trigo"]
#
#qtde_vezes = lista_compras.count("leite") #conta quantas vezes o elemento aparece dentro da lista
#idx = lista_compras.index("leite") #em qual indice da lista o elemento está
#
#print("Quantidade: ", qtde_vezes)
#print("Primeiro idx: ", idx)

#ordenando. é possível ordenar os elementos da lista usando sort()
#lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]
#for item in lista_compras:
#    print(item)

#ordenando a lista em ordem alfabetica
#print("Ordenado") 
#lista_compras.sort()
#for item in lista_compras:
#    print(item)

#ordenando a lista em ordem descrescente (alfabetica ao contrario)
#print("Ordenado Decrescente")
#lista_compras.sort(reverse = True)
#for item in lista_compras:
#    print(item)

#excluindo por indice
#Para excluir um elemento da lista por indice, utilize del nome_lista[idx]
#lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]
#del lista_compras[1]
#for item in lista_compras:
#    print(item)

#excluindo por valor
#lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]

#lista_compras.remove("arroz") #a função remove(conteudo) remove o primeiro elemento com o conteudo especificado
#lista_compras.pop() #a função pop() remove o ultimo elemento

#for item in lista_compras:
#    print(item)

#inserindo
lista_compras = ["maçãs", "leite", "arroz", "frango", "trigo"]

lista_compras.insert(2, "feijão") # insert(idx, item) insere o item na posição e desloca o restante da lista para a direita
lista_compras.append("tomate") # append(item) insere o item no final

for item in lista_compras:
    print(item)