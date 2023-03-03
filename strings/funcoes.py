# Algumas funções úteis

# Len
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

# Replace
# A função replace() permite modificar o trecho de uma frase, gerando uma string nova com a modificação e mantendo a string original não alterada
# frase = "Estou fazendo um curso de Java, porque eu gosto de Java"
# mudanca = frase.replace("Java", "Python")
# mudanca_espec = frase.replace("Java", "Python", 1) --> possibilita especificar o número limite de substituições feitas na frase
# print(frase) --> frase original
# print(mudanca) --> frase alterada

# Concatenação
# É possível concatenar strings utilizando o operador '+' ou a pontuação ','
# Exemplo:
# curso = "Python"
# saudacao = "Bom dia!"
# frase = saudacao + "Esse é um curso de " +  curso + "."
# print(frase)
# print(saudacao,"Esse é um curso de", curso, ".")

# Caracteres de controle
# Os caracteres de controle agem sem necessariamente imprimir algo na tela
# Em Python, um caractere de controle começo com um barra invertida \
# "\n" insere uma quebra de linha
# "\t" insere uma tabulação --> um espaço maior
# Exemplo:
# frase = "Esse é um texto\nde\texemplo"
# print(frase)

# Caixa
# É possível tranformar a caixa dos caracteres de uma string, sendo caixa baixa --> lower(), caixa alta --> upper() ou deixar a primeira letra maiúscula e as demais minúsculas --> capitalize()
# Exemplo:
# frase = "CURSO de Python"
# print(frase.lower())
# print(frase.upper())
# print(frase.capitalize())

# Split --> string de quebra
# A função split() é utilizada para quebrar uma string em uma lista de strings
# Exemplo:
#frase = "Esse é o curso de Python - Foco em iniciantes"
#lista1 = frase.split(" ") # ao passar a função com um espaço, está pedindo que a função quebra toda vez que encontrar um espaço na string
#for item in lista1:
#    print(item)
#lista2 = frase.split("-") # ao passar a função com um -, está pedindo que a função quebra toda vez que encontrar um - na string
#for item in lista2:
#    print(item)

# índice ???
# Para encontrar o índice de uma palavra ou caractere, use a função find()
# Exemplo
# frase = "Olá mundo teste isso vai ficar teste final"
# inicio = frase.find("teste") + len("teste") # função para encontrar o indice da string teste e descolar o indice até o final da string, sendo a própria palavra teste ???
# fim = frase.find("teste", inicio) # procure a palavra "teste", mas a partir de determinado ponto, sendo esse ponto a função "inicio"
# print(frase[inicio:fim])
