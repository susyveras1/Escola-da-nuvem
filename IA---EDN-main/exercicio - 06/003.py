'''3 - Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
** Instale o modulo requests - pip install requests **
URL da API ViaCEP, passando o CEP informado
    url = f"https://viacep.com.br/ws/{cep}/json/"'''
    
import requests

# Solicita o CEP ao usuário
cep = input("Digite o CEP (apenas números): ")

# Valida se o CEP tem 8 dígitos
if len(cep) == 8 and cep.isdigit():
    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "erro" not in dados:
            print("\nInformações do Endereço:")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado (UF): {dados.get('uf', 'Não disponível')}")
        else:
            print("❌ CEP não encontrado.")
    else:
        print("Erro na requisição à API.")
else:
    print("❌ CEP inválido. Certifique-se de digitar 8 números.")
