#lista_compras = ["maçãs", "leite", "arroz", "frango"]

# for i in range(len(lista_compras)):
#    print("O elemento ", i, "da lista é", lista_compras[i])

lista_compras = ["maçãs", "leite", "arroz", "frango", "macarrão"]

#alterando o valor de um elemento da lista
lista_compras[1] = "batatas"
lista_compras[0] = "laranjas"

sublista = lista_compras[0:4] #definindo o intervalo da sublista
print("Sublista")
for item in sublista:
    print(item)

print("Outra forma")
for item in lista_compras[2:6]:
    print(item)