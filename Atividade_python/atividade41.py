# Exercício 41
numero = int(input("Digite um número inteiro positivo: "))

if numero < 1:
    print("Número inválido. Digite um inteiro positivo.")
else:
    for i in range(1, numero + 1):
        print(i)