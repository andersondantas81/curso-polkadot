
# Exercício 4:
# Escreva um programa que peça a temperatura atual e diga se está quente (acima de 30°C), frio (abaixo de 15°C) ou 
# agradável (entre 15°C e 30°C).

temperatura = float(input("Informe a temperatura atual em grau Celsius: "))

if temperatura > 30:
  print("Hoje está quente")
elif temperatura < 15:
  print("Hoje está frio")
else :
  print("Hoje está agradável")


