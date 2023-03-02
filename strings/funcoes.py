# Algumas funções úteis

# A função len() retorna o tamanho da string em número de caracteres
# Exemplo:
# frase = "Curso de Python"
# print("Número de caracteres: ", len(frase))

# Para acessar a posição de um caractere de uma string, é possível acessar por índice, como em vetores
# Exemplo
# frase = "Curso de Python"
# print("Primeira letra: ", frase[0])
# linguagem = frase[9:len(frase)] # mostra a partir do caractere/índice 9 até o final da frase
# print("Do caractere 9 até o final: ", linguagem)

# A função replace() permite modificar o trecho de uma frase, gerando uma string nova com a modificação e mantendo a string original não alterada
# frase = "Estou fazendo um curso de Java, porque eu gosto de Java"
# mudanca = frase.replace("Java", "Python")
# print(frase)
# print(mudanca)