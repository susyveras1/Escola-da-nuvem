# 006 - Crie um programa que receba um número do usuário e diga se ele é positivo, negativo ou igual a zero.

# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou igual a zero
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é igual a zero.")
