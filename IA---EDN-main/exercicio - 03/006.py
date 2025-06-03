'''6 - Crie um programa que simula a validação de uma senha usando um loop while True. O usuário tem no máximo 3 tentativas. Use break para encerrar o loop quando a senha for correta ou quando o número máximo de tentativas for atingido.'''

senha_correta = "segredo"
tentativas = 0  # Contador de tentativas

while True:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    elif tentativas == 3:
        print("Número máximo de tentativas atingido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")
