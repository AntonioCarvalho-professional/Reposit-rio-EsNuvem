def main():
    pi = 3.14159265
    try:
        raio = float(input())
        area = pi * (raio ** 2)
        print(f"A={area:.4f}")
    except ValueError:
        print("Por favor, insira um número válido para o raio.")

if __name__ == "__main__":
    main()
