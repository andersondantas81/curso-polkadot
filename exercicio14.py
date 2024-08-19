# Exercício 14:
# Crie um programa que verifique se uma palavra ou 
# frase é um palíndromo.

def palindromo(frase):
  palavra = frase.split()
  invertido = palavra[::-1]
  junto = ' '.join(invertido)
 
  return junto
    

print(palindromo(str(input("Digite uma palavra ou frase: ")).strip().upper()))
print(palindromo("radar"))
