# Exercício 64
import random

numeros = [random.randint(1, 100) for _ in range(10)]
multiplos_de_3 = [n for n in numeros if n % 3 == 0]

print("Números sorteados:", numeros)
print("Múltiplos de 3:", multiplos_de_3)