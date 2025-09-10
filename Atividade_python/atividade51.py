# Exercício 51
soma = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma dos números digitados é {soma}.")