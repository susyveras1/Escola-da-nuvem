'''1 - Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.'''

import random
import string

def gerar_senha(tamanho):
    # Combina letras, dígitos e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Solicita ao usuário o tamanho da senha
try:
    tamanho = int(input("Informe o número de caracteres para a senha: "))
    if tamanho < 1:
        print("Por favor, digite um número maior que zero.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, digite um número válido.")
