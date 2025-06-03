'''7- Verificador de Palíndromo
Enunciado:
Crie um programa que solicite uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).'''

# Solicita a palavra ao usuário
palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")
