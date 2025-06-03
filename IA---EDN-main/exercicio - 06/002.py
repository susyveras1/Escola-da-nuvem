'''2 - Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
** Instale o modulo requests - pip install requests **
URL da API que retorna um usuário aleatório no formato JSON
    url = "https://randomuser.me/api/"'''
    
import requests

# Pergunta ao usuário quantos perfis deseja gerar
quantidade = int(input("Quantos perfis de usuário você quer gerar? "))

# Gera os perfis
for i in range(quantidade):
    url = "https://randomuser.me/api/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        nome_completo = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        pais = user['location']['country']

        print(f"\nPerfil {i + 1}:")
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print(f"\nErro ao acessar a API no perfil {i + 1}.")
