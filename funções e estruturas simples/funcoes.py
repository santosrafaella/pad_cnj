# funções estão sendo usadas o tempo todo
# função é uma sequência de instruções para realizar uma dada tarefa
# print() é uma função
# math.sqrt() é uma função
# input() é uma função
# def é uma palavra reservada para criar uma nova função

# def saudacao():
#   print("Olá, bem vindo!")
#    print("Esse é o curso de Python.")
#
#saudacao()

# Uma função comumente possui parâmetros --> ()
# def saudacao(nome, periodo):
#    if (periodo == 'm'):
#        print("Bom dia, ", nome, "!")
#    elif(periodo == 't'):
#        print("Boa tarde, ", nome, "!")
#    elif(periodo == 'n'):
#        print("Boa noite, ", nome, "!")
#    else:
#       print("Ops, período inválido!")
#    print("Esse é o curso de Python.")

#saudacao("Rafaella", 'n')

# Valores default
# Os parâmetros da função podem ter valores default (padrão)
# Para usa um valor padrão use:
# nome_par = valor_padrao

# def saudacao(nome, periodo = 'm'):
#    if (periodo == 'm'):
#        print("Bom dia, ", nome, "!")
#    elif(periodo == 't'):
#        print("Boa tarde, ", nome, "!")
#    elif(periodo == 'n'):
#        print("Boa noite, ", nome, "!")
#    else:
#       print("Ops, período inválido!")
#    print("Esse é o curso de Python.")

#saudacao("Rafaella")

#Fatorial
def fatorial (n):
    res = 1
    while(n> 1):
        res = res*n
        n = n - 1
    print("O fatorial de", valor, "é: ", res)

valor = int(input("Digite um valor ou -1 para sair: "))
while(valor != -1):
    fatorial(valor)
    valor = int(input("Digite um valor ou -1 para sair: "))