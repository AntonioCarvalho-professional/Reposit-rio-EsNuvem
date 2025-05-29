import requests

def consultar_endereco_por_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança exceção para códigos de erro HTTP
        dados = resposta.json()

        if "erro" in dados:
            print("❌ CEP não encontrado.")
            return

        print("\n📍 Endereço encontrado:")
        print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
        print(f"Bairro: {dados.get('bairro', 'Não informado')}")
        print(f"Cidade: {dados.get('localidade', 'Não informado')}")
        print(f"Estado: {dados.get('uf', 'Não informado')}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao conectar com a API ViaCEP: {erro}")

# Execução do programa
if __name__ == "__main__":
    while True:
        cep = input("Digite o CEP (somente números) ou 'sair' para encerrar: ").strip()
        if cep.lower() == "sair":
            print("Encerrando...")
            break
        if not cep.isdigit() or len(cep) != 8:
            print("❗ CEP inválido. Digite exatamente 8 números.")
            continue
        consultar_endereco_por_cep(cep)
