# Exercício 17
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
if num2 != 0:
    print("Divisão:", num1 / num2)
else:
    print("Divisão: impossível (divisão por zero)")