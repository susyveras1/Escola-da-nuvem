'''3 - Crie uma função que calcule a idade de uma pessoa em dias, com base no ano de nascimento informado pelo usuário.
O programa deve considerar o ano atual como base para o cálculo.
Use try/except para tratar erros de entrada e valide que o ano não pode ser maior que o ano atual.'''

from datetime import datetime

# Função para calcular a idade em dias
def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação sem considerar anos bissextos
    return idade_dias

# Programa principal
def main():
    ano_atual = datetime.now().year
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        
        if ano_nascimento > ano_atual:
            print("Erro: O ano de nascimento não pode ser maior que o ano atual.")
        else:
            idade_dias = calcular_idade_em_dias(ano_nascimento)
            print(f"Você tem aproximadamente {idade_dias} dias de vida.")
    
    except ValueError:
        print("Erro: Entrada inválida. Digite um ano válido (somente números).")

# Executa o programa
main()
