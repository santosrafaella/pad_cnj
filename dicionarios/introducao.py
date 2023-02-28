# Dicionários

# Dicionário é uma coleção não-ordenada de "valores" indexados por "chaves"
# Exemplo: em um dicionário real, as chaves seriam as palavras e os valores os significados das palavras
# Dicionários se parecem com listas, mas são mais versáteis
# l1 = ["a", "b", "c"] --> lista
# print(list(enumerate(l1))) #função usada para mostrar o índice e seu respectivo elemento
# O dicionário é uma coleção não ordenada, porque diferente da lista que tem os índices em ordem [0][1][2][3], os dicionários são organizados por chaves que são definidas pelo programador, pois são strings
# Estrutura de um dicionário:
# Dic = {}
# Sempre terá que inserir a chave e o valor. exemplo:
# Dic = {'chave1': 'valor1', 'chave2': 'valor2'} --> dicionário com 2 elementos
# Função para adicionar outra chave no dicionário:
# Dic['chave3'] = 'valor3'
# Caso seja feita uma atribuição de valor para uma chave que já existe, esse valor será atualizado
# Função para remover elemento:
# Dic.pop('chave1')
# Função para remover o último elemento:
# Dic.popitem()
# Outro método para remover um elemento específico:
# del Dic['chave3']
# A função del também é usada para remover um dicionário inteiro:
# del Dic
# print(chave) #imprime apenas as chaves do dicionário
# print(dic1[chave]) #imprime apenas os valores do dicionário
# print(chave, dic1[chave]) #imprime os dois componentes, tanto da chave quanto dos valores, uma por linha
# Funções que retornam listas dos componentes do dicionário:
# dic.keys () #retorna uma lista com as chaves do dicionário
# dic.values () #retorna uma lista com os valores do dicionário
# dic.items() #retorna uma tupla com as chaves e valores, imutavél
# Um dicionário em Python garante a ordem de inserção, ou seja, os item são organizados de acordo com a ordem em que são inseridos.


