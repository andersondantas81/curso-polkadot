# Exercício 20:
# Escreva um programa que peça ao usuário um número inteiro 
# e informe se ele é par ou ímpar

num =  int(input("informe um número: "))

if num % 2 == 0:
  print(f" O número {num} é par.")
else:
  print(f" O número {num} é ímpar.")