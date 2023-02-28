Dic = {'chave1': 'valor1', 'chave2': 'valor2'}
#print(Dic['chave2']) --> como chamar uma chave específica
Dic['chave3'] = 'valor3' # --> adicionando uma chave nova no dicionário
Dic['chave3'] = 'valorX' # --> atribuir um valor diferente a uma chave já existente, fará com que o valor seja atualizado e reatribuido
Dic.pop('chave1') # --> função para remover um elemento específico
#Dic.popitem() # --> função que remove o último elemento de um dicionário
del Dic['chave3'] # --> outra forma de remover um elemento específico
print(Dic)