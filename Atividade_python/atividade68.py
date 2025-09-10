# Exercício 68 - Cadastro de Alunos
import uuid

alunos = {}

def cadastrar_aluno():
    nome = input("Nome: ")
    email = input("E-mail: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    matricula = str(uuid.uuid4())[:8]
    alunos[matricula] = {"nome": nome, "email": email, "nascimento": nascimento}
    print(f"Aluno cadastrado! Matrícula: {matricula}")

def atualizar_aluno():
    matricula = input("Digite a matrícula: ")
    if matricula in alunos:
        print("Dados atuais:", alunos[matricula])
        campo = input("Qual campo deseja atualizar (nome/email/nascimento)? ")
        if campo in alunos[matricula]:
            valor = input(f"Novo valor para {campo}: ")
            alunos[matricula][campo] = valor
            print("Dados atualizados com sucesso!")
        else:
            print("Campo inválido.")
    else:
        print("Matrícula não encontrada.")

def remover_aluno():
    matricula = input("Digite a matrícula: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso.")
    else:
        print("Matrícula não encontrada.")

def listar_alunos():
    if alunos:
        for mat, dados in alunos.items():
            print(f"\nMatrícula: {mat}")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
    else:
        print("Nenhum aluno cadastrado.")

def mostrar_aluno():
    matricula = input("Digite a matrícula: ")
    if matricula in alunos:
        print("Dados do aluno:")
        for chave, valor in alunos[matricula].items():
            print(f"{chave.capitalize()}: {valor}")
    else:
        print("Matrícula não encontrada.")

while True:
    print("\nMenu:")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar aluno")
    print("3 - Remover aluno")
    print("4 - Listar todos os alunos")
    print("5 - Mostrar aluno por matrícula")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        atualizar_aluno()
    elif opcao == "3":
        remover_aluno()
    elif opcao == "4":
        listar_alunos()
    elif opcao == "5":
        mostrar_aluno()
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")