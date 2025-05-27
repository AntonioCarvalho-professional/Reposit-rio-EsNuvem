def main():
    try:
        nome = input("Nome do vendedor: ").strip()
        salario_fixo = float(input("Salário fixo: R$ "))
        total_vendas = float(input("Total de vendas: R$ "))

        comissao = total_vendas * 0.15
        total_receber = salario_fixo + comissao

        print(f"TOTAL = R$ {total_receber:.2f}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para salário e vendas.")

if __name__ == "__main__":
    main()
