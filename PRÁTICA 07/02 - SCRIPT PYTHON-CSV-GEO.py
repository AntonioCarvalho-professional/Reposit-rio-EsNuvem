import csv

# Dados a serem escritos
pessoas = [
    {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 34, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"}
]

# Nome do arquivo CSV
nome_arquivo = 'pessoas.csv'

# Escreve os dados no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

    escritor.writeheader()  # Escreve o cabeçalho
    for pessoa in pessoas:
        escritor.writerow(pessoa)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
