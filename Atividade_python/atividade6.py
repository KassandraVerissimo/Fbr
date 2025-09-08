# Exercício 6
operacao = input("Digite a operação (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    print("Resultado:", num1 + num2)
elif operacao == "-":
    print("Resultado:", num1 - num2)
elif operacao == "*":
    print("Resultado:", num1 * num2)
elif operacao == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero!")
else:
    print("Operação inválida!")
