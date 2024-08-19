# Exercício 27: 
# Escreva um programa que verifique se um número 
# dado é um número perfeito.

numero = int(input("Informe um número: "))
perf = []

for n in range(1, numero):
  div = numero % n

  if div == 0:
    perf.append(n)

print(perf)