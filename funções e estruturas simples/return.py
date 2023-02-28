# Return é uma palavra chave para retornar um resultado dentro da função
# Quando uma função retorna(termina) imediatamente ao encontrar um return
# O formato é:
# return valor_a_ser_retornado

# fatorial melhorado
import matematica #importando a função fatorial que está no arquivo matemática

valor = int(input("Digite um valor ou -1 para sair: "))
while(valor != -1):
    resultado = matematica.fatorial(valor)
    print("O fatorial de", valor, "é", resultado)
valor = int(input("Digite um valor ou -1 para sair: "))