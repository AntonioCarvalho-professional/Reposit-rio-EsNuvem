def calcular_desconto(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return valor_desconto, preco_final

def main():
    produto = "Camiseta"
    preco = 50.00
    desconto_percentual = 20

    desconto, preco_com_desconto = calcular_desconto(preco, desconto_percentual)

    print(f"Produto: {produto}")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Desconto aplicado: {desconto_percentual}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")

if __name__ == "__main__":
    main()
