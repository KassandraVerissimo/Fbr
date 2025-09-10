# Exercício 49
contador = 0
for i in range(7):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero > 10:
        contador += 1

print(f"Você digitou {contador} números maiores que 10.")