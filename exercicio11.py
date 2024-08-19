# Exercício 11:
# Escreva um programa que peça um número inteiro ao usuário e 
# calcule o fatorial desse número.

def fatorial():
  num = int(input("Informe um número: "))
  fat = 1

  for i in range(1, num+1):
    fat = fat * i 
  print(fat)

fatorial()

