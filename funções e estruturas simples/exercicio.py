#exercicio 1
# def funcao(lista):
#    fim = len(lista)-1
#    inicio = 0
#    while (inicio < fim):
#        aux = lista[inicio]
#        lista[inicio] = lista[fim]
#        lista[fim] = aux
#        inicio = inicio + 1
#        fim = fim - 1

#exercicio 2
# def minha_funcao(valor):
#        if(valor == 1):
#                return valor + 1;
#        valor = valor + 10
#        return valor + 20

#a = 1
#resultado = minha_funcao(a)
#print(resultado)

#exercicio 3
#objetos = ("cadeira", "mesa", "vaso")
#objetos.remove("cadeira")
#objetos.append("caneta")
#del objetos[0]

#exercicio 4
# def funcao(a, b):
#        a = a + 1
#        b[1] = a
    
# def imprimir(lista):
#        for item in lista:
                #o end = seguido de duas aspas simples serve para não pular de linha
#                print(item, ' ', end= '')
#        print()

#var = 10
#lista = [1,2,3]
#funcao(var, lista)
#print(var)
#imprimir(lista)

#exercicio 5
lista = [1,2,58,10,19,30,58,100]

lista.remove(58)

del lista[1]

lista.append(-3)

lista.insert(2, 77)

lista.insert(2, 77)

print(lista)