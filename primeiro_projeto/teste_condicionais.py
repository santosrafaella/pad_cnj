# Operadores de comparação + operadores lógicos
idade = int (input("Digite sua idade: "))
if idade >= 18:
    print("Permitido dirigir no Brasil!")
if idade < 18:
    print("Não é permitido dirigir no Brasil!")
if idade > 15:
    print("Permitido dirigir nos EUA!")
if (idade >= 16) and (idade < 21): #ambas condições devem ser  satisfeitas para que o operador AND resulte em uma expressão satisfeita no final
    print("Permitido dirigir, mas proibido compra álcool nos EUA") #só entra nesse bloco se as duas condições forem verdadeiras, caso contrário esse bloco será desconsiderado