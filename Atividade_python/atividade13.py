# Exercício 13
mes = int(input("Digite um número de 1 a 12 para o mês: "))

if mes in [12, 1, 2]:
    print("Estação: Verão")
elif mes in [3, 4, 5]:
    print("Estação: Outono")
elif mes in [6, 7, 8]:
    print("Estação: Inverno")
elif mes in [9, 10, 11]:
    print("Estação: Primavera")
else:
    print("Mês inválido!")