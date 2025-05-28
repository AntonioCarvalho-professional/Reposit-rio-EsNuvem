import string

def verificar_palindromo(texto: str) -> str:
    # Remove pontuações e espaços, e converte para minúsculo
    tabela = str.maketrans('', '', string.punctuation)
    texto_limpo = texto.translate(tabela).replace(" ", "").lower()
    
    # Verifica se o texto é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso:
if __name__ == "__main__":
    entrada = input("Digite uma palavra ou frase: ")
    resultado = verificar_palindromo(entrada)
    print(resultado)
