# Exercício 9:
# Escreva um programa que peça uma frase ao usuário e conte quantas vezes 
# uma letra específica aparece.

texto = input("Digite uma frase: ")

def buscarQuatLetra(letra):
  contador = 0
  for l in list(texto.upper()):
    if l == letra.upper() :
      contador += 1
  
  print(f"A letra {letra} aparece {contador} na frase.")
    
  

buscarQuatLetra('A')
buscarQuatLetra('c')