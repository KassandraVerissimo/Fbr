# Exercício 57
import random

secreto = random.randint(1, 10)
palpite = 0

while palpite != secreto:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    if palpite != secreto:
        print("Tente novamente!")

print(f"Parabéns! O número secreto era {secreto}.")