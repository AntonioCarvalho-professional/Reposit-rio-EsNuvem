def main():
    try:
        notas = list(map(float, input("10.0 4.9 9.5 9.8  ").split()))
        if len(notas) != 4:
            print("Você deve digitar exatamente 4 notas.")
            return

        pesos = [2, 3, 4, 1]
        media = sum(n * p f*
