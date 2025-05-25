def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

def main():
    try:
        peso = float(input("Digite o peso (kg): "))
        altura = float(input("Digite a altura (m): "))

        imc = peso / (altura ** 2)
        classificacao = classificar_imc(imc)

        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    main()
