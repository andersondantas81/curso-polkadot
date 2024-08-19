# Exercício 13:
# Escreva um programa que peça o peso e a altura de uma pessoa e 
# calcule seu Índice de Massa Corporal (IMC).

def IMC(): 
  peso = float(input("Informe seu peso(kg): "))
  altura = float(input("Informe sua altura(m): "))

  imc = peso / (altura * altura)

  if imc >  40:
    print("obesidade grau III ou mórbida.")
  elif imc>= 35 and imc <=39.9 :
        print("obesidade grau II ou severa")
  elif imc>= 30 and imc <=34.9 :
        print("obesidade grau I")
  elif imc>= 25 and imc <=29.9 :
        print("sobrepeso")
  elif imc>= 18.6 and imc <=24.9 :
        print("peso ideal")
  elif imc>= 17 and imc <=18.5 :
        print("magreza leve")
  elif imc>= 16 and imc <=16.9 :
        print("magreza moderada")
  else:
    print("magreza grave")

IMC()