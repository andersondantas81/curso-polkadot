# Exercício 29:
# Crie um programa que calcule a média ponderada de três notas 
# fornecidas pelo usuário, considerando os pesos 2, 3 e 5.

notas = list()
pesos = [2, 3, 5]
denominadorP = 0
divisorP = 0
for i in range(1, 4):
  notas.append(int(input(f"Informe a i° nota: ")))

for j in range(0, 3):
  denominadorP += notas[j]*pesos[j]
  divisorP += pesos[j]

mediaP = denominadorP / divisorP
print(f"A média ponderada é  {mediaP}")