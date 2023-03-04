# Formas de formatar uma função

# Uma forma de formatar um string é usar o format()
# A forma mais simples de usar o format é colocando {} na string, pois as chaves servem como placeholders e serão substituídas pelo format()
# A função format() retorna uma nova string com o conteúdo substituído
# Exemplo:
#anterior = 5000
#atual = 5500
#diferenca = atual - anterior
#porcentagem = diferenca/anterior * 100
#frase = "A diferença de salário é de R${}, ou seja, {}%" #neste caso o {} será substituído pelos valores da diferença e da porcentagem
#formatado = frase.format(diferenca, porcentagem)
#print(formatado)

# Outra forma de formatar (mais usada) é usar o format() diretamente no print
# Exemplo:
#salario = 7500
#print("O seu salário é {}.".format(salario))

# Outra maneira
#anterior = 5000
#atual = 5500
#diferenca = atual - anterior
#porcentagem = diferenca/anterior * 100
#print("A diferença de salário é de R${}, ou seja, {}%".format(diferenca, porcentagem))

# Impressão de variáveis específicas
salario = 7500
#print("O seu salário é {:f}.".format(salario)) # dessa forma é possível forçar o formart() a imprimir um tipo específico de variável, no caso do exemplo, transformando em um float
#print("O seu salário é {:.2f}.".format(salario)) # dessa forma, uma variável float será inserido com dois decimais
