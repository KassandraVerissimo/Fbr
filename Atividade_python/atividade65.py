# Exercício 65
numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))