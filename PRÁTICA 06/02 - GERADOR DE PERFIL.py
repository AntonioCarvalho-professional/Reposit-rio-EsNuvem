import requests

def gerar_usuario_aleatorio():
    try:
        resposta = requests.get("https://randomuser.me/api/")
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil Gerado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    except (KeyError, IndexError) as e:
        print(f"Erro ao processar os dados recebidos: {e}")

# Executa a função
gerar_usuario_aleatorio()

