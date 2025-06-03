'''2 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
A função deve receber dois parâmetros:
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (por exemplo, 10 para 10%)'''

# Função que calcula a gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso
def main():
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
    
    gorjeta = calcular_gorjeta(valor_conta, porcentagem)
    total = valor_conta + gorjeta

    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar (conta + gorjeta): R$ {total:.2f}")

# Executa o programa
main()
