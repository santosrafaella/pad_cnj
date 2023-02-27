#exercicio 1
#for num in range (10):
#    if (num/2 == 0):
#        print(num)

#exercicio 2
#n = 2
#for i in range(10):
#    produto = n*i
#    print(produto)

#exercicio 3
#i = 0
#while i <= 10:
#    print(i)
#    i += 1

#exercicio 4
#if(aparelho == 'tv'):
#    if(marca == 'sony'):
#        if(tamanho == 48):
#            print('Equipamento:', aparelho, marca, tamanho)
#    else: 
#        tamanho = 50
#elif(marca == 'samsung'):
#    print('Equipamento:', aparelho, marca, tamanho)
#
#else:
#        print('Equipamento:', aparelho, marca, tamanho)

#exercicio 5
idade = int(input("Digite sua idade: "))
if idade >= 18:
        print("Pode dirigir no Brasil...")
if idade < 18:
        print("Não pode dirigir no Brasil!")
if idade > 15:
        print("Pode dirigir nos EUA...")
if idade >= 16 and idade < 21:
        print("Pode dirigir, mas não comprar álcool nos EUA")