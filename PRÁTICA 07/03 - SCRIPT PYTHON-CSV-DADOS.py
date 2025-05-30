import csv

# Nome do arquivo CSV
nome_arquivo = 'pessoas.csv'

# Lê e exibe os dados do arquivo CSV
with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    
    print("Dados do arquivo CSV:\n")
    for linha in leitor:
        nome = linha['Nome']
        idade = linha['Idade']
        cidade = linha['Cidade']
        print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
