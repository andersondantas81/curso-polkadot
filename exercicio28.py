# Exercício 28:
# Desenvolva um programa que conte quantas palavras há em uma 
# frase fornecida pelo usuário.

frase = input("Informe uma frase: ")
palavras = frase.split()
print(len(palavras))
quant = 0

for palavra in palavras:
    
    if ',' in palavra or ';' in palavra or ':' in palavra or '.' in palavra or '?' in palavra or '!' in palavra:      
        if len(palavra[:-1]) > 0:
          print(palavra[:-1])
          quant = quant + 1
    else:
        print(palavra)
        quant = quant + 1

print(quant)