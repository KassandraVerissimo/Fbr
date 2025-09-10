# Exercício 45
numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

print("O maior número é:", max(numeros))