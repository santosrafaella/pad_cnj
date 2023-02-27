print("Olá!")
nome = input("Digite seu nome: ")
print("Bem vindo", nome)
idade = int(input("Qual sua idade? ")) # o int () serve para converter uma string em int
print("Você tem", idade, "anos.")
aposentadoria = int(input("E com qual idade você espera se aposentar? "))
print("Então você tem ", idade, "anos e quer se aposentar com ", aposentadoria)
anos_faltantes = aposentadoria - idade
print("Faltam ", anos_faltantes, "anos para voê se aposentar, ", nome)

