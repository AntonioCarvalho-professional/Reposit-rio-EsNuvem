def classificar_idade(idade):
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida"

def main():
    try:
        idade = int(input("Digite a sua idade: "))
        categoria = classificar_idade(idade)
        print(f"Categoria: {categoria}")
    except ValueError:
        print("Por favor, digite um número inteiro válido para a idade.")

if __name__ == "__main__":
    main()
