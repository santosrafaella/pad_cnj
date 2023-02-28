dicio = {2: 'b', 1: 'a', 3: 'c'}

#dicio[2] = "b"
#dicio[1] = "a"
#dicio[3] = "c"

#o print(dicio) #imprime na ordem de inserção, na ordem em que os elementos foram adicionados
#o print(sorted(dicio)) retorna apenas as chaves organizadas
#o print(dict(sorted(dicio.items()))) #retorna o dicionário organizado por ordem alfabética
#o dicio = dict(sorted(dicio.items())) atribui um novo valor ao dicionário dicio e deixa todos os componentes organizados por ordem alfabética independente da ordem de inserção
#o print(sorted(dicio.items())) #retorna uma lista de tuplas organizada em ordem de valor (1,2,3)
#o print(sorted(dicio, key=dicio.get)) #ordena as chaves por valor
dicio_ordenado = {}
print(sorted(dicio, key=dicio.get)) #ordena as chaves por valor