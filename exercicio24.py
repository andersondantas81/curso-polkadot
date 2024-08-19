# Exercício 24: 
# Crie um programa que funcione como uma calculadora simples, 
# pedindo ao usuário dois números e a operação que deseja realizar
 
def calculadora():
  num = int(input("Informe o primeiro número: "))
  num2 = int(input("Informe o segundo número: "))
  op = input("Informe a operação: (+, -, *, /): ")

  match op:
    case '+':
        print(f"{num} + {num2} = {num + num2}")
    case '-':
        print(f"{num} - {num2} = {num - num2}")
    case '*':
        print(f"{num} * {num2} = {num * num2}")
    case '/':
        print(f"{num} / {num2} = {num / num2}")
    case _:
        print("Unknown Valor")

calculadora()