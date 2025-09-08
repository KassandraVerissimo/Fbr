# Exercício 16
combustivel = input("Digite o tipo de combustível (gasolina, etanol, diesel): ").lower()

if combustivel == "gasolina":
    print("Preço: R$ 5,80 por litro")
elif combustivel == "etanol":
    print("Preço: R$ 4,20 por litro")
elif combustivel == "diesel":
    print("Preço: R$ 4,90 por litro")
else:
    print("Combustível não reconhecido.")