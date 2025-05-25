def calcular_consumo(distancia_km, combustivel_litros):
    consumo_medio = distancia_km / combustivel_litros
    return round(consumo_medio, 2)

def main():
    distancia = 300  # km
    combustivel = 25  # litros

    consumo = calcular_consumo(distancia, combustivel)

    print("Dados da Viagem:")
    print(f"Distância percorrida: {distancia} km")
    print(f"Combustível gasto: {combustivel} litros")
    print(f"Consumo médio: {consumo:.2f} km/l")

if __name__ == "__main__":
    main()
