# Exercício 12:
# Crie um programa que converta uma temperatura dada em Celsius 
# para Fahrenheit e Kelvin.

def conversorTemperatura():
    
  celsius = int(input("Informe a temperatura em graus Celsius(°C): "))
  fahrenheit = (celsius * 9/5) + 32
  kelvin = celsius + 273.15

  print (f"Fahrenheit: {fahrenheit} °F - Kelvin: {kelvin} K")
  
conversorTemperatura()
