def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def converter_temperatura(valor, unidade_origem, unidade_destino):
    unidade_origem = unidade_origem.lower()
    unidade_destino = unidade_destino.lower()

    if unidade_origem == unidade_destino:
        return valor

    if unidade_origem == 'c':
        if unidade_destino == 'f':
            return celsius_para_fahrenheit(valor)
        elif unidade_destino == 'k':
            return celsius_para_kelvin(valor)

    elif unidade_origem == 'f':
        if unidade_destino == 'c':
            return fahrenheit_para_celsius(valor)
        elif unidade_destino == 'k':
            return fahrenheit_para_kelvin(valor)

    elif unidade_origem == 'k':
        if unidade_destino == 'c':
            return kelvin_para_celsius(valor)
        elif unidade_destino == 'f':
            return kelvin_para_fahrenheit(valor)

    return None  # Caso inválido

def main():
    try:
        valor = float(input("Digite a temperatura: "))
        unidade_origem = input("Unidade de origem (C, F, K): ").strip()
        unidade_destino = input("Unidade para converter (C, F, K): ").strip()

        resultado = converter_temperatura(valor, unidade_origem, unidade_destino)

        if resultado is not None:
            print(f"{valor:.2f}°{unidade_origem.upper()} = {resultado:.2f}°{unidade_destino.upper()}")
        else:
            print("Unidade inválida. Use apenas C, F ou K.")
    except ValueError:
        print("Digite um valor numérico válido para a temperatura.")

if __name__ == "__main__":
    main()
