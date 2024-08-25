# Exercício 31:
# Instruções: Você foi contratado pela equipe de segurança digital da Polkadot 
# para ajudar a decifrar um código secreto que protege as transações em DOT. 
# O código foi gerado por um algoritmo que segue regras específicas para somar 
# ou subtrair números dentro de um intervalo. Sua missão é criar um programa 
# em Python que possa decifrar esse código aplicando as regras fornecidas.

inicial = int(input("Digite o número inicial do intervalo: "))
final = int(input("Digite o número final do intervalo: "))
total = 0

for i in range(inicial, final+1):
  if i % 3 == 0:
    total += i
  elif i % 5 == 0:
    total = abs(total - i)
  else:
    pass

print(f"O valor total calculado : {total}")

#Readme
# Com um for o programa percorre o intervalo informado pelo usuário e
# e através e com a estrutura condicional if, elfi e else é verificado 
# se o resto da divisão é zero se for de 3 ou 5, respectivamente é realizado 
# a soma ou subtração. Foi utilizado a funçao abs() para obter um valor
# absoluto(valor não negativo) para que a subtração não fique negativa em 
# algumas condições. Como o exercício pedia else, eu colquei o else e a instrução
# pass que é uma declaração nula que funciona como um espaço reservado 
# quando uma instrução é sintaticamente necessária, mas não é necessário 
# código real, ou seja, para qualque outra condição inclusive quando os valores
# forem multiplos de 3 e 5 ao msmo tempo o programa vai desconsiderar.