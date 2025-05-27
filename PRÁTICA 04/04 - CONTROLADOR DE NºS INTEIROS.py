def classificar_numeros():
    pares = 0
    impares = 0

    print("Digite números inteiros (ou 'fim' para encerrar):")

    while True:
        entrada = input("Número: ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print("É par.")
                pares += 1
            else:
                print("É ímpar.")
                impares += 1
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

    print("\nResumo:")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Executar o programa
classificar_numeros()
