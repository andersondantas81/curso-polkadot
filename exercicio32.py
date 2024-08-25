# Exercício 32:
# Um desenvolvedor da Polkadot escondeu um número mágico na rede que pode 
# aumentar os ganhos em staking de DOT. Esse número segue regras 
# específicas e está escondido dentro de um intervalo de números inteiros. Sua missão é criar um programa em Python que consiga identificar esse "Número Mágico" e revelar as novas oportunidades de staking.

# Regras do Desafio:
# 1. O "Número Mágico" é o primeiro número dentro de um intervalo que atende a todas as condições abaixo:
# 2. É divisível por 4.
# 3. É um número primo.
# 4. A soma dos dígitos do número é um número ímpar.
# 5. Se nenhum número no intervalo atender a todas essas condições, o programa deverá informar que o "Número Mágico" não foi encontrado.

inicial = int(input("Digite o número inicial do intervalo: "))
final = int(input("Digite o número final do intervalo: "))
cont = True
soma = 0

def isPrimo(num):
  if num < 2:
      return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
    return True


def somarDigitos(num):
  qtdDigitos = len(str(num))
  for i in list(str(num)):
    soma += int(i)
    print(soma)

  if soma % 3 == 0: 
    print(soma)
    return True
  else: 
    return False

for i in range(inicial, final+1):
  if i % 4 == 0:
    if isPrimo(i):
      print(i, " é primo")
      if somarDigitos(i):
        cont = False
        break
if cont:
  print("Nenhum número mágico foi encontrado no intervalo.")


  # README
   # o programa sempre exibirá a mensagem: Nenhum número mágico foi encontrado no intervalo.
   # poís não existe número primo divisível por 4