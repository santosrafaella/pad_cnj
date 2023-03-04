# Arquivos Delimitados

# Você pode criar seu próprio padrão de arquivos, mas em sistemas simples é mais comum a utuilização de padrões já conhecidos e bema aceitos, como csv, xml, Json,...

# Arquivos CSV
# CSV - comma-separated values
# Tipo de arquivo de texto delimitado
# É um arquivo texto onde os valores são separados por vírgula
# Muitas vezes usamos outros separadores como ;
# Exemplo:
#Nome;Idade;Salário # header/cabeçalho --> opcional, porém recomendado
#Rafaella Santos;45;8500, 85 # ; sendo usado para separar para não confundir com a , dos valores
#José Oliveira;30;5500, 4
#Marcos Santos;35;8000

# Exemplo:
arq = open("exemplo.csv", "r")
arq.readline() #descartando primeira linha

idades = 0
salarios = 0
qtde = 0
for linha in arq:
    quebra = linha.split(';')
    idades = idades + int(quebra[1])
    salarios = salarios + float(quebra[2].replace(',','.'))
    qtde = qtde + 1
arq.close()

print("A idade média é: ", idades/qtde)
print("O salário médio é: ", salarios/qtde)

# VOLTAR VÍDEO "ARQUIVOS DELIMITADOS" NO MINUTO 2:08