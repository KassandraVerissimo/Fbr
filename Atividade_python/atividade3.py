# Exercício 3
dias = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

numero = int(input("Digite um número de 1 a 7 para o dia da semana: "))

if numero in dias:
    print(f"O dia correspondente é: {dias[numero]}")
else:
    print("Número inválido! Digite de 1 a 7.")