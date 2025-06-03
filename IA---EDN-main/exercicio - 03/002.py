'''2 - Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando a estrutura de repetição for.'''

numero = int(input("Digite um número para ver a tabuada: "))

# Laço para multiplicar o número de 1 até 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
