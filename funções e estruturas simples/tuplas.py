# Tuplas
# Similares a listas, porém são imutáveis
# Depois de fazer uma tupla, você não pode fazer modificações
# Deve usar uma tupla quando precisar que uma "lista" não seja modificada
# Tuplas são mais eficientes do que listas
# Uma tupla é definida com ()

tupla_compras = ("maçãs", "leite", "arroz", "frango", "trigo")

for item in tupla_compras:
    print(item)

print("O item 1 é: ", tupla_compras[1])