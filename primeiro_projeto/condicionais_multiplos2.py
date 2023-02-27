a = int(input("Digite um valor para 'A': "))
b = int(input("Digite um valor para 'B': "))

if (a > b):
    print("A é maior do que B ({} > {})".format(a,b))
#cadeia if-elif-else
#elif é usado para testar mais de duas condições
#pode usar quantos elif forem necessários, porém só pode haver um if e um else
elif (a < b):
    print("B é maior do que A ({} > {})".format(b,a))
else:
    print("A e B são iguais!")