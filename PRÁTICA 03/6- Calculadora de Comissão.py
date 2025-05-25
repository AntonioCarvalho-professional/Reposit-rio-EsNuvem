def main():
    try:
        nome = input("Antonio Lobo: ").strip()
        salario_fixo = float(input(" R$ 3.000,00 "))
        total_vendas = float(input(" R$ 5.000,00 "))

        comissao = total_vendas * 0.15
        total_receber = salario_fixo + comissao

        print(f"TOTAL = R$ {total_receber:.2f}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para salário e vendas.")

if __name__ == "__main__":
    main()
