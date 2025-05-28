from datetime import datetime

def idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Desconsiderando anos bissextos
    return idade_dias

# Exemplo de uso
try:
    ano = int(input("Digite o ano de nascimento: "))
    dias = idade_em_dias(ano)
    print(f"Idade aproximada em dias: {dias} dias")
except ValueError:
    print("Por favor, digite um ano válido.")
