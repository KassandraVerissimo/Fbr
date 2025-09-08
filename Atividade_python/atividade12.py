# Exercício 12
transporte = input("Escolha um modo de transporte (carro, bicicleta, a pé): ").lower()

if transporte == "carro":
    print("Velocidade média: 80 km/h")
elif transporte == "bicicleta":
    print("Velocidade média: 20 km/h")
elif transporte == "a pé":
    print("Velocidade média: 5 km/h")
else:
    print("Transporte não reconhecido.")