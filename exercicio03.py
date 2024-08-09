# Exercício 3:
# Escreva um programa que peça dois números ao usuário e exiba a soma, 
# subtração, multiplicação e divisão deles.

while True:
  print ("1 - Soma, 2 - subtração, 3 - multiplicação ou 4 - divisão ")
  operacao = input("Informe um número de 1 a 5 para definir a operação deseja realizar ? ")
  if (int(operacao) > 0 and int(operacao) < 5):
    n1 = input("Informe o primeiro número: ")
    n2 = input("Informe o segundo número: ")
    break

match int(operacao):
    case 1:
        print(f"Resultado = {int(n1) + int(n2)}")
    case 2:
        print(f"Resultado = {int(n1) - int(n2)}")
    case 3:
        print(f"Resultado = {int(n1) * int(n2)}")
    case 4:
        print(f"Resultado = {int(n1) / int(n2)}")
    case _:
        print("Unknown Valor")