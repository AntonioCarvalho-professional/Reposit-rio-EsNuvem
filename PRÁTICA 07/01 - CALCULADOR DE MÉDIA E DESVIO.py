import re
import statistics

# Lê o arquivo
with open('log.txt', 'r') as file:
    linhas = file.readlines()

# Extrai os tempos de execução usando expressão regular
tempos = []
for linha in linhas:
    match = re.search(r'([\d.]+)\s*segundos', linha)
    if match:
        tempo = float(match.group(1))
        tempos.append(tempo)

# Calcula média e desvio padrão
media = statistics.mean(tempos)
desvio_padrao = statistics.stdev(tempos)

# Exibe os resultados
print(f"Média do tempo de execução: {media:.2f} segundos")
print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
