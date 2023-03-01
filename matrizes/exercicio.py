# Considere um arquivo de texto a ser passado pelo usuário via argumento na linha de comando:
# a. Crie um contador de palavras onde cada palavra é uma chave em um dicionário e a frequência de ocorrência é o valor a se armazenar na chave.
# b. Crie um contador de caracteres (todos, incluindo sinais de pontuação e espaço) que mostre, ao final, o número total de caracteres do texto e a frequência individual de cada um (use um dicionário).
# c. Imprima o dicionário de palavras em ordem alfabética inversa (de Z para A)
# d. Imprima o dicionário de caracteres em ordem alfabética.

texto = input("Insira um texto: ")
print("\n\n", texto)
print("A quanitdade de palavras no texto é: ", len(texto.split()))
print("A quantidade de caraceteres com espaço no texto é: ", len(texto))
