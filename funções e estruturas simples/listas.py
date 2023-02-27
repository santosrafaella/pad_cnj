# Estrutura de dados para criar listas em python
# nome_lista = [item1, item2, item3]
# Os itens se manterão na ordem em que você definir
# Exceto que você peça explicitamente para alterar a ordem

# cada item desta lista é uma string, então usar aspas
#lista_compras = ["maçãs", "leite", "arroz", "frango"]

# Passar item por item da lista (iterar)
#for item in lista_compras:
#    print("Comprar: ", item)

# é possível passar por cada item da lista usando os indices, para isso utilize o operador [], lembrando que os operadores começam no indice 0
#lista_compras = ["maçãs", "leite", "arroz", "frango"]
#print("O primeiro item que preciso comprar é :", lista_compras[2])

# A função len() retorna o tamanho de uma lista

lista_compras = ["maçãs", "leite", "arroz", "frango", "banana"]

tamanho = len(lista_compras)
print("A lista de compras possui: ", tamanho, "itens.")
print("E o último item da lista é: ", lista_compras[len(lista_compras)-1]) #acessa o último item da lista