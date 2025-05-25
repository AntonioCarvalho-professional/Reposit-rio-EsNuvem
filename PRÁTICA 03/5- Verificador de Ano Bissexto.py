def ano_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

def main():
    try:
        ano = int(input("Digite o ano: "))
        if ano_bissexto(ano):
            print(f"{ano} é bissexto.")
        else:
            print(f"{ano} não é bissexto.")
    except ValueError:
        print("Por favor, digite um ano válido (número inteiro).")

if __na
