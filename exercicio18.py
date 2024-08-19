# Exercício 18:
# Escreva um programa que mostre os primeiros n números da 
# sequência de Fibonacci, onde n é informado pelo usuário.

n = int(input("Informe o número de sequências de Fibonacci: "))
t1 = 0
t2 = 1
cont = 3

print(f'{t1} -> {t2}', end='')

while cont <= n:
  t3 = t1 + t2
  print(f' -> {t3}', end='')
  t1 =t2
  t2 =t3
  cont += 1
print(" ->FIM")