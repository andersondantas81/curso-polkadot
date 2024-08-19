# Exercício 16:
# Crie um programa que peça uma frase ao usuário e conte 
# quantas vogais (a, e, i, o, u) ela contém.

import unicodedata
frase = input("Informe uma frase: ")
frase = unicodedata.normalize('NFKD', frase).encode('ascii', 'ignore').decode('ascii')
cont = 0

for i in list(frase.lower()):
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    cont = cont + 1

print(f"A frase contém {cont} vogal(is).")