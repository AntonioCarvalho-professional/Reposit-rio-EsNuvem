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
        if unidade_destino == 'f_'
