# Exercício 69 - Jogo da Velha Avançado
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vencedor(tabuleiro, jogador):
    combinacoes = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],  # linhas
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],  # colunas
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]                        # diagonais
    ]
    return any(all(tabuleiro[x][y] == jogador for x,y in comb) for comb in combinacoes)

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"

    for turno in range(9):
        exibir_tabuleiro(tabuleiro)
        while True:
            try:
                linha = int(input(f"Jogador {jogador}, linha (0-2): "))
                coluna = int(input(f"Jogador {jogador}, coluna (0-2): "))
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador
                    break
                else:
                    print("Posição já ocupada, tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida, digite entre 0 e 2.")

        if verificar_vencedor(tabuleiro, jogador):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            return

        jogador = "O" if jogador == "X" else "X"

    exibir_tabuleiro(tabuleiro)
    print("Empate!")

while True:
    jogar()
    repetir = input("Deseja jogar novamente? (s/n): ").lower()
    if repetir != "s":
        print("Fim do jogo!")
        break