# Exercício 66
cadastros = []

while True:
    print("\nMenu:")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar nomes")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome para cadastrar: ")
        cadastros.append(nome)
        print("Nome cadastrado com sucesso!")

    elif opcao == "2":
        antigo = input("Digite o nome que deseja atualizar: ")
        if antigo in cadastros:
            novo = input("Digite o novo nome: ")
            indice = cadastros.index(antigo)
            cadastros[indice] = novo
            print("Nome atualizado com sucesso!")
        else:
            print("Nome não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome que deseja excluir: ")
        if nome in cadastros:
            cadastros.remove(nome)
            print("Nome excluído com sucesso!")
        else:
            print("Nome não encontrado.")

    elif opcao == "4":
        print("Lista de cadastrados:", cadastros)

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")