# Exercício 67 - Jogo da Velha
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador = "X"

for _ in range(9):
    exibir_tabuleiro(tabuleiro)
    linha = int(input(f"Jogador {jogador}, escolha a linha (0-2): "))
    coluna = int(input(f"Jogador {jogador}, escolha a coluna (0-2): "))

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        if verificar_vencedor(tabuleiro, jogador):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            break
        jogador = "O" if jogador == "X" else "X"
    else:
        print("Posição ocupada, tente novamente.")
else:
    exibir_tabuleiro(tabuleiro)
    print("Empate!")