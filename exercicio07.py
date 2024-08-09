# Exercício 7:
# Crie uma lista de compras que permita ao usuário adicionar itens e, 
# em seguida, imprimir a lista completa.

lista = []
def adicionar(item):
  lista.append(item)
  print(f"Minha lista de compras: {lista}")

adicionar("Arroz")
adicionar("Feijão")
adicionar("Macarrão")
adicionar("Carne")