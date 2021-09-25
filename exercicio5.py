# Elevar um número ao expoente

numero = int(input("Digite o número base:"))
expoente = int(input("Digite o expoente:"))
x = range(expoente-1)
numerocalculado = numero

for n in x:
  numerocalculado = numerocalculado * numero

print("O resultado o cálculo exponencial é: ", numerocalculado)