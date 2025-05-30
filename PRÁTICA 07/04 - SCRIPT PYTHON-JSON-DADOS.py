import json

# Dados da pessoa
pessoa = {
    "nome": "Lucas",
    "idade": 30,
    "cidade": "Fortaleza"
}

# Nome do arquivo JSON
nome_arquivo = 'pessoa.json'

# Escreve os dados no arquivo JSON
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
    json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)

print("Dados salvos com sucesso em 'pessoa.json'.\n")

# Lê os dados do arquivo JSON
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
    dados_lidos = json.load(arquivo_json)

print("Dados lidos do arquivo JSON:")
print(f"Nome: {dados_lidos['nome']}")
print(f"Idade: {dados_lidos['idade']}")
print(f"Cidade: {dados_lidos['cidade']}")
