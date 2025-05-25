def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return round(media, 2)

def main():
    nota1 = 7.5
    nota2 = 8.0
    nota3 = 6.5

    media_final = calcular_media(nota1, nota2, nota3)

    print("Notas do aluno:")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média final: {media_final:.2f}")

if __name__ == "__main__":
    main()
