# Exercício 33:
# Você foi encarregado de criar uma versão digital de um jogo de bingo 
# para a comunidade Polkadot. No Bingo da Adivinhação, o computador 
# sorteia números aleatórios, e você deverá tentar adivinhar os números 
# sorteados para completar sua carteira de DOT. Quem conseguir adivinhar 
# todos os números da sua cartela primeiro garante a transferência segura 
# dos seus fundos.

import random

cartela = list()
cont = 0

for i in range(1, 6):
  cartela.append(random.randint(1, 75))
print(f"Sua cartela: {cartela}")

while len(cartela) >= 1:
  sorteado = random.randint(1, 75)
  cont += 1
  print(f"Número sorteado: {sorteado}")
  for i in list(cartela):
    if sorteado == i:
      cartela.remove(i)
      if len(cartela) == 0:
        print(f"Você acertou {i}! Números restantes na cartela: {cartela}")
        print(f"Parabéns! Você completou sua cartela em {cont} sorteios.")
      else:
        print(f"Você acertou {i}! Números restantes na cartela: {cartela}")
        
# README
# 1- É criado uma lista com 5 números randômicos 
# 2 - Enquanto ea lista não estiver vazia é executado a funça randmint
# para obter um número entre 1 e 75 e incremento um contador para saber
# no final quantos números foram obtidos. Percorre toda a lista verificando 
# se o número existe se existir exibe a mensagem e remove o número da lista
# faz esse processo até a lista ficar vazia, entra no else e exibe a mensagem de parabéns.