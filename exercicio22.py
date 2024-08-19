# Exercício 22:
# Crie um jogo onde o programa escolhe um número aleatório 
# entre 1 e 100, e o usuário deve adivinhar qual é o número.

# import random
from random import randint

sorteado = randint(1, 100)
palpite = int(input("Der seu palpite: "))

if sorteado == palpite:
  print(f"Parabéns, você acertou !")
else:
  print(f"Não foi dessa vez, o número sorteado foi {sorteado}")