# Exercício 25: 
# Escreva um programa que peça ao usuário um número n e calcule a 
# soma dos primeiros n números naturais.

n=int(input("Digite um número positivo e inteiro: "))
soma = 0
if n > 0:
  for i in range(n+1):
    soma = soma + i
    print("para n = ",i," a soma é: ", soma)
  print("A soma dos ",n," primeiros números naturais é: ",soma)
elif n < 0:
  print("Somente para números positivos!")