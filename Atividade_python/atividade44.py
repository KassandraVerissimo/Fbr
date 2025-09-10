# Exercício 44
pares = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        pares.append(numero)

print("Números pares digitados:", pares)