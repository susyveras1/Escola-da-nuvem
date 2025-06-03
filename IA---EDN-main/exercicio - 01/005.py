# 05 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de acordo com a operação escolhida.

# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Escolha a operação (+, -, * ou /): ")

# Realiza a operação de acordo com a escolha
if operacao == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida.")
