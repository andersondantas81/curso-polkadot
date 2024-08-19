# Exercício 30:
# Escreva um programa que peça ao usuário uma lista de números e, 
# ao final, exiba o maior, o menor, e a média dos números inseridos.

numeros = []

n = int(input("Adicione um número ou digite -1 para sair: "))
while n != -1:
  numeros.append(n)
  n = int(input("Adicione um número ou digite -1 para sair: "))

def mergeSort(numeros):
    print("Splitting ",numeros)
    if len(numeros)>1:
        mid = len(numeros)//2
        lefthalf = numeros[:mid]
        righthalf = numeros[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numeros[k]=lefthalf[i]
                i=i+1
            else:
                numeros[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numeros[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numeros[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",numeros)


mergeSort(numeros)
print(numeros)
print(f"O menor valor é {numeros[0]}")
print(f"O maior valor é {numeros[len(numeros)-1]}")
soma = 0 
for s in numeros:
  soma = soma + s
print(f"A média é {soma / len(numeros)}")