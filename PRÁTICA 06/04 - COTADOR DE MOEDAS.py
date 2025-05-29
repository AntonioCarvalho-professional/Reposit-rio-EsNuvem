import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        par = f"{moeda}BRL"
        if par not in dados:
            print("❌ Código de moeda inválido ou não disponível.")
            return

        cotacao = dados[par]
        print(f"\n💱 Cotação atual de {moeda} para BRL:")
        print(f"→ Valor atual: R$ {cotacao['bid']}")
        print(f"→ Valor máximo: R$ {cotacao['high']}")
        print(f"→ Valor mínimo: R$ {cotacao['low']}")
        print(f"📅 Data da última atualização: {cotacao['create_date']}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")

# Execução principal
if __name__ == "__main__":
    while True:
        moeda = input("\nDigite o código da moeda (ex: USD, EUR, GBP) ou 'sair' para encerrar: ").strip()
        if moeda.lower() == 'sair':
            print("Encerrando...")
            break
        elif len(moeda) != 3:
            print("❗ Código de moeda inválido. Use três letras (ex: USD).")
            continue
        else:
            consultar_cotacao(moeda)
