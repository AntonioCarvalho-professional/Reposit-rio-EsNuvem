def main():
    try:
        notas = list(map(float, input("Digite as quatro notas separadas por espaço: ").split()))
        if len(notas) != 4:
            print("Você deve digitar exatamente 4 notas.")
            return

        pesos = [2, 3, 4, 1]
        media = sum(n * p for n, p in zip(notas, pesos)) / 10
        print(f"Media: {media:.1f}")

        if media >= 7.0:
            print("Aluno aprovado.")
        elif media < 5.0:
            print("Aluno reprovado.")
        else:
            print("Aluno em exame.")
            exame = float(input("Nota do exame: "))
            print(f"Nota do exame: {exame:.1f}")
            media_final = (media + exame) / 2
            if media_final >= 5.0:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
            print(f"Media final: {media_final:.1f}")
    except ValueError:
        print("Erro: Digite somente números válidos com ponto decimal.")

if __name__ == "__main__":
    main()
