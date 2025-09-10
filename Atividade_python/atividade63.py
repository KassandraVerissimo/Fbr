# Exercício 63
numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Soma dos números:", sum(numeros))