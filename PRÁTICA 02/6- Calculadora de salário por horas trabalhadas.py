def main():
    try:
        numero_funcionario = int(input("Número do funcionário: "))
        horas_trabalhadas = int(input("Horas trabalhadas: "))
        valor_por_hora = float(input("Valor recebido por hora: "))

        salario = horas_trabalhadas * valor_por_hora

        print(f"NUMBER = {numero_funcionario}")
        print(f"SALARY = R$ {salario:.2f}")
    except ValueError:
        print("Por favor, insira os valores no formato correto.")

if __name__ == "__main__":
    main()
