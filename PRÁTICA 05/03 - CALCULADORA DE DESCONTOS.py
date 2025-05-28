def calcular_preco_final(preco_original: float, percentual_desconto: float) -> float:
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return preco_final

# Entrada do usuário
try:
    preco = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o percentual de desconto: "))

    preco_com_desconto = calcular_preco_final(preco, desconto)
    print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")

except ValueError:
    print("Entrada inválida. Certifique-se de digitar números válidos.")
