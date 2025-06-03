# 007 - Crie um programa que contenha uma lista com números e calcule a soma total desses números usando um laço for.

# Lista com números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializa a variável que armazenará a soma
soma_total = 0

# Laço for para somar os números
for numero in numeros:
    soma_total += numero

# Exibe o resultado da soma
print(f"A soma total dos números é: {soma_total}")
