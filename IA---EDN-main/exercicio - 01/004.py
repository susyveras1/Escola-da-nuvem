# 004 - Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário.

# Define a função que retorna o dobro do número
def dobrar(numero):
    return numero * 2

# Solicita um número ao usuário
numero_usuario = float(input("Digite um número: "))

# Chama a função e exibe o resultado
resultado = dobrar(numero_usuario)
print(f"O dobro de {numero_usuario} é {resultado}.")
