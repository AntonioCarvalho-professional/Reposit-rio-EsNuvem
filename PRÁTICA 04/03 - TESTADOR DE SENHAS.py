def senha_forte():
    print("Verificador de senha forte.")
    print("Regras: mínimo 8 caracteres e pelo menos um número.")
    print("Digite 'sair' para encerrar.")

    while True:
        senha = input("Digite uma senha: ")

        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break

        if len(senha) < 8:
            print("Senha muito curta! Mínimo de 8 caracteres.")
            continue

        if not any(char.isdigit() for char in senha):
            print("Senha fraca! Deve conter pelo menos um número.")
            continue

        print("Senha forte registrada com sucesso!")
        break

# Executar o programa
senha_forte()
