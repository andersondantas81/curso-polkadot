# Exercício 19:
# Crie um programa que leia três números diferentes e os 
# imprima em ordem crescente.

def bubble_sort(v):
  cont=0
  fim = len(v)
  while fim > 0:
    i = 0
    while i < fim - 1:
      if v[i] > v[i + 1]:
        v[i], v[i + 1] = v[i + 1], v[i]
      i += 1
    fim -= 1
    cont += 1
    if v[0]< v[1] < v[2]:
      break
  return v


listaNumeros = list()
for c in range(1, 4):
    listaNumeros.append(int(input(f'Digite o {c}º valor: ')))

print(bubble_sort(listaNumeros))
