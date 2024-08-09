# Exercício 8:
# Escreva uma função que receba um número e retorne se ele é par ou ímpar.

def paridade(num):

  if num % 2 == 0:
    print(f"O número {num} é par.")
  else:
    print(f"O número {num} é ímpar.")

paridade(1)
paridade(2)