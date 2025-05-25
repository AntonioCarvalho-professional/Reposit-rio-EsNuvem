def main():
    try:
        A = int(input("Digite o valor inteiro A: "))
        B = int(input("Digite o valor inteiro B: "))

        X = A + B
        print(f"X = {X}")
    except ValueError:
        print("Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
