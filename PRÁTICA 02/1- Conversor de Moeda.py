def conversor_moeda(valor_reais, taxa_dolar, taxa_euro):
    valor_em_dolar = valor_reais / taxa_dolar
    valor_em_euro = valor_reais / taxa_euro

    return round(valor_em_dolar, 2), round(valor_em_euro, 2)

def main():
    valor_reais = 100.00
    taxa_dolar = 5.65
    taxa_euro = 6.15

    dolar, euro = conversor_moeda(valor_reais, taxa_dolar, taxa_euro)

    print(f"Valor em Reais: R$ {valor_reais:.2f}")
    print(f"Convertido em Dólares: US$ {dolar:.2f}")
    print(f"Convertido em Euros: € {euro:.2f}")

if __name__ == "__main__":
    main()
