# Define uma função chamada "media" que recebe dois parâmetros: n1 e n2
def media(n1, n2):
    return (n1 + n2) / 2  # Soma as duas notas e divide por 2 para calcular a média

# Solicita ao usuário a primeira nota
n1 = float(input("Primeira nota: "))  # input() recebe o valor como texto, float() converte para número decimal

# Solicita ao usuário a segunda nota
n2 = float(input("Segunda nota: "))  # mesma lógica da linha anterior

# Exibe o resultado da média na tela
print("Média:", media(n1, n2))  # Chama a função passando n1 e n2, e imprime o resultado com a mensagem "Média:"