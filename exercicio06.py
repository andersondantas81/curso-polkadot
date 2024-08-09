# Exercício 6:
# Crie um programa que pergunte ao usuário por números até que ele digite zero 
# e então mostre a soma dos números digitados.

acumulador = 0
while True:

  numero  = int(input("Informe um número diferente de zero ou digite 0 para finalizar: "))
  if (numero != 0):
   acumulador += numero 
  else:
    break
print(f"A soma dos números digitados é {acumulador}")