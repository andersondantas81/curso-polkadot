# Exercício 10:
# Crie um programa que encontre e imprima todos os números primos em um 
# intervalo definido pelo usuário.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def numeros_primos():
  while True :
    num1 = int(input("Informe o primeiro número do range maior que 1: "))
    if num1 > 1:
      break

  while True :
    num2 = int(input("Informe o segundo número do range maior que " +str(num1)+": "))
    if num2 > num1:
      break

  listaPrimos = []
  for i in range(num1, num2 + 1):
    if is_prime(i):
      listaPrimos.append(i)

  print(f"O(s) número(s) {listaPrimos} é(são) primo(s).")


numeros_primos()