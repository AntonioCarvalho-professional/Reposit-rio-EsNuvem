def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
try:
    valor = float(input("Informe o valor total da conta: R$ "))
    porcentagem = float(input("Informe a porcentagem da gorjeta (%): "))
    valor_gorjeta = calcular_gorjeta(valor, porcentagem)
    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
