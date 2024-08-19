# Exercício 15:
# Escreva um programa que exiba a tabuada de um número 
# fornecido pelo usuário.

def tabuada():
  num = int(input("Informe um número de 1 - 10: "))
  op = input("Informe a operação: (+, -, *, /): ")

  match op:
    case '+':
        for i in range(1, 11):
          print(f"{num} + {i} = {num + i}")
    case '-':
        for i in range(1, 11):
          print(f"{num} - {i} = {num - i}")
    case '*':
        for i in range(1, 11):
          print(f"{num} * {i} = {num * i}")
    case '/':
        for i in range(1, 11):
          print(f"{num} / {i} = {num / i}")
    case _:
        print("Unknown Valor")

tabuada()