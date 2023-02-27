#exemplo 1 do comando while
#n =  int(input("Digite um número inteiro: "))
#while (n > 0):
#    print(n)
#    #equivalente a n = n-1
#    n -= 1 #decremento com reatribuição. subtrai e reatribui o valor de n
#print("Tempo esgotado")

#exemplo 2 do comando while com loop infinito porém tem como sair 
#while(True):
#
#   letra = input("Digite uma letra diferente de 'q': ")
#    if (letra == 'q'):
#        break
#print("Você digitou a letra 'q'!!!")

#exemplo 3 do comando while forçado a saída de um laço
cond = True

while (cond):
    opcao = input("Digite 'sair' para terminar o laço.")
    if opcao == 'sair':
        cond = False
    else:
        print("Ainda no laço...")