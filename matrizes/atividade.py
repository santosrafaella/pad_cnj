# Atividade 1

#carro = 'honda'
#cor = 'prata'

#if not(carro == 'honda' and carro == 'toyota'):
#    print("Correto")
#else:
#    print("Incorreto")

#if (carro == 'honda' or carro == 'toyota'):
#    print("Correto")
#else:
#    print("Incorreto")

#if (carro == 'honda' and carro == "toyota"):
#    print("Correto")
#else:
#    print("Incorreto")

#if not(carro == 'honda' or carro == 'toyota'):
#    print("Correto")
#else:
#    print("Incorreto")

#if(carro == 'honda'  or  carro == 'toyota') and (cor == 'prata'):
#    print("Correto")
#else:
#    print("Incorreto")

# Atividade 2

#carro = 'civic'

#if carro.lower() == 'civic':
#    print('Acertou')

#print('Vamos andar de {}'.format(carro))

#carro = 'civic'

#if carro.lower() == 'civic':
    #if carro.upper() == 'civic':
# if carro.title() == 'civic':
#if carro.capitalize() == 'civic':
#    print(carro)

#carro = 'honda'
#cor = 'prata'

#if (carro == 'honda'):
#    print("Acertou")

#    if(cor != 'prata'):
#        print("Outra cor")
#    else:
#       print(cor.title())
#else:
#    print("Outro carro")

#pessoa1 = 15
#pessoa2 = 17
#papel1 = 'menor'
#papel2 = 'responsável'

#if ((pessoa1 >= 18) or (pessoa2 >= 18)) and  ((papel1 == 'responsável') or (papel2 == 'responsável')) and not ((pessoa1 < 12) or (pessoa2 < 12)):
#    print("Ambos assistem ao filme no cinema")
#else:
#    print("Não assiste")

#carro = 'civic'

#if(carro.lower() == 'civic'):
#    print('Acertou')
#else:
#    print('Errou')
#if(carro.upper() == 'civic'):
#    print('Acertou')
#else:
#    print('Errou')
#if(carro.title() == 'civic'):
#    print('Acertou')
#else:
#    print('Errou')
#if(carro.capitalize() == 'civic'):
#    print('Acertou')
#else:
#    print('Errou')


texto = "My my, hey hey Rock and roll is here to stay It's better to burn out than to fade away My my, hey hey Out of the blue and into the black They give you this, but you pay for that An' once you're gone you can never come back When you're out of the blue and into the black The king is gone, but he's not forgotten This is the story of a Johnny Rotten It's better to burn out than it is to rust The king is gone, but he's not forgotten Hey hey, my my Rock and roll can never die There's more to the picture than meets the eye Hey hey, my my"

texto = texto.replace("á","a")
texto = texto.replace("à","a")
texto = texto.replace("ã","a")
texto = texto.replace("é","e")
texto = texto.replace("ê","e")
texto = texto.replace("í","i")
texto = texto.replace("ó","o")
texto = texto.replace("ô","o")
texto = texto.replace("ú","u")

vogais = 0

for caracter in texto:
    if caracter in 'aeiou':
        vogais = vogais + 1
print ("Vogais: %d" %vogais)   


# def vogais(texto):
#    vogais = ['a', 'e', 'i', 'o', 'u']
#    return texto.lower() in vogais
#print(