# Exercício 33
valor = float(input("Digite o valor do produto: R$ "))
desconto = valor * 0.10
valor_final = valor - desconto
print(f"Valor com desconto de 10%: R$ {valor_final:.2f}")