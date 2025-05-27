def calculadora():
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: entrada inválida. Digite um número válido.")

    while True:
        try:
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: entrada inválida. Digite um número válido.")

    while True:
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
            break
        elif operacao == "-":
            resultado = num1 - num2
            break
        elif operacao == "*":
            resultado = num1 * num2
            break
        elif operacao == "/":
            try:
                resultado = num1 / num2
                break
            except ZeroDivisionError:
                print("Erro: divisão por zero não é permitida.")
        else:
            print("Erro: operação inválida. Tente novamente.")

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")

# Executar a calculadora
calculadora()
