# Modo de escrita

# Para abrir um arquivo texto no modo escrita existem dois modos básicos:
# Se o arquivo não existir ao ser aberto no modo escrita, um arquivo novo será criado
# Modo escrita (write). Se você abrir um arquivo existente no modo escrita, esse arquivo será substituído  --> f = open(nomeArquivo, "w")
# Modo anexagem (append). Se você abrir um arquivo existente no modo escrita, o conteúdo escrito será anexado no final do arquivo --> f = open(nomeArquivo, "a")
# Para fechar um arquivo, será usado o arq.close()

# A função write() não adiciona uma quebra de linha no texto, então caso você vá escrever um arquivo existente, será necessário adicionar uma quebra de linha no início da função
# A função write() só aceita strings. Caso precise inserir uma variável diferente, converta para string usando str()
# Exemplo:
valor = 10
pi = 3.14
nome = "Rafaella Santos"

arq = open("documento_escrita.txt", "a") #abriu o arquivo no modo escrita
arq.write(str(valor)) # escreveu o valor
arq.write('; ') # escreveu o ;
arq.write(str(pi)) # escreveu o pi
arq.write('; ') # escreveu o ;
arq.write(nome) # escreveu o nome
arq.write('\n') # pulou uma linha no texto
arq.close() # fechou o arquivo