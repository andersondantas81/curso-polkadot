# Exercício 17:
# Desenvolva um programa que calcule a média de várias notas 
# inseridas pelo usuário. O programa deve parar de pedir notas 
# quando o usuário digitar -1.

nota = 0
cont = 0
n = 0

while n != -1:
  n = float(input('Informe uma nota ou digite -1 para sair: '))
  if n != -1:
    nota = nota + n
    cont = cont + 1

print(f"A média é {nota/cont}")