'''3 - Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0, mostrando cada número. Ao final, exibir "FIM!".'''

import time
import sys

# Foguete
foguete = [
    "     ^     ",
    "    / \\    ",
    "   / _ \\   ",
    "  | (_) |  ",
    "  |  |  |  ",
    "  |  |  |  ",
    " /|__|__|\\ ",
    "/_________\\",
    "    | |     ",
    "   /   \\    "
]

numero = int(input("Digite um número para contagem regressiva: "))

# Contagem decrescente
for i in range(numero, -1, -1):
    print(i)
    time.sleep(1)  # Pausa de 1 segundo entre os números

# Início do foguete subindo
print("FIM!")
time.sleep(1)

# Animação de foguete saindo da base
altura_max = 10  # Máxima altura que o foguete pode alcançar
espaco = [" " * len(foguete[0])] * altura_max  # espaço vazio para o foguete subir

# Animação
for i in range(altura_max):
    sys.stdout.write("\033[F")  # Move o cursor para cima
    # Exibe o foguete subindo
    for j in range(altura_max - i):
        print(espaco[j])  # Imprime os espaços vazios antes do foguete
    for linha in foguete:
        print(linha)  # Imprime o foguete
    time.sleep(0.2)  # Tempo para dar a sensação de movimento
    if i < altura_max - 1:
        foguete = [" " * len(linha) for linha in foguete]  # Limpa a tela do foguete para o movimento

# Efeito de decolagem
print("🚀 Foguete decolando... BOOM! 💥")