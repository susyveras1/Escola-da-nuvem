'''4 - Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
** Instale o modulo requests - pip install requests **
URL da API com base na moeda informada
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"'''
    
import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    chave = f"{moeda}BRL"
    
    if chave in dados:
        cotacao = dados[chave]
        
        # Convertendo para float e formatando com vírgula
        valor_atual = float(cotacao['bid'])
        valor_max = float(cotacao['high'])
        valor_min = float(cotacao['low'])
        
        print("\n===== Cotação Atual =====")
        print(f"Moeda: {moeda} / BRL")
        print(f"Valor Atual: R$ {valor_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Máximo do Dia: R$ {valor_max:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Mínimo do Dia: R$ {valor_min:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Última Atualização: {cotacao['create_date']}")
        print("=========================\n")
    else:
        print(f"❌ Moeda '{moeda}' não encontrada. Verifique o código e tente novamente.")
else:
    print("❌ Erro ao consultar a API. Tente novamente mais tarde.")
