opcao = input("Forma de pagamento [c|d|b|o]: ") #c - crédito (0% desc) | d - débito (3% desc) | b - boleto (5% desc) | o - dinheiro (10% desc)
if (opcao == 'c'):
    print("Pagamento no crédito sem desconto.")
elif (opcao == 'd'):
    print("Pagamento no débito com 3% de desconto.")
elif (opcao == 'b'):
    print("Pagamento no boleto com 5% de desconto.")
elif (opcao == 'o'):
    print("Pagamento no dinheiro com 10% de desconto.")
else:
    print("Opção '{}'a não cadastrada.".format(opcao))