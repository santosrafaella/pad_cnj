# Abrindo e fechando arquivos de texto

# Para abrir um arquivo texto no modo leitura, use a função arq = open(nomeArquivo, "r")
# arq é uma variável que representa o arquivo aberto
# r é de read e indica que o arquivo será de leitura
# É obrigatório que o arquivo seja fechado após ser usado, usando a função arq.close()
# Exemplo:
# arq = open("documento.txt", "r")
# Faz algo com o arquivo
# arq.close()

# Read --> não muito usual
# A função read() lê todo o conteúdo do arquivo
# Exemplo:
#arq = open("documento.txt", "r")
#conteudo = arq.read()
#print(conteudo)
#arq.close()

# Readline
# A função readline() é usada para ler uma única linha, ela retorna a próxima linha do arquivo ou uma string vazia se o arquivo terminou
#arq = open("documento.txt", "r")
#conteudo = arq.readline() # ela iniciará a leitura de uma linha, ele só lerá a próxima linha se eu chamar a função novamente
#while(conteudo != ""):
#    print("Linha lida:", conteudo)
#    conteudo = arq.readline()
#arq.close()

# Iteração
# É possível iterar linha a linha de um arquivo
#Exemplo:
#arq = open("documento.txt", "r")
#for linha in arq:
#    print("Linha lida:", linha)
#arq.close()
# Esse exemplo faz a mesma coisa que o readline, porém é mais consiso e deixa que o próprio python faça algumas coisas

# Exemplo utilizando outras funções
arq = open("documento.txt", "r") # leu o arquivo
for linha in arq: # pegando o arquivo linha a linha
    quebra = linha.split(" ") # está dando um espaço entre os itens do arquivo e transformando o item da linha 1 em uma lista
    nome = quebra[0] # lendo o item que está no índice 0
    idade = int(quebra[1]) # lendo o item que está no índice 1 e transformar a váriavel string em número inteiro
    print(nome, "tem", idade, "anos de idade.")
arq.close()