#Exemplo de testes condicionais dentro de teste já existentes
idade = int(input("Digite sua idade: "))

if (idade >= 16):
    print("Você já pode votar se tiver um título de eleitor.")
    if (idade >= 18 and idade <= 70):
        print("Se você é alfabetizado, seu voto é obrigatório!")
    else:
        print("Seu voto é facultativo.")
else:
    print("Você ainda não pode votar.")