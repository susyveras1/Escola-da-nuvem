'''4 - Crie um programa que continue pedindo uma senha ao usuário até que ele digite a senha correta. Quando isso acontecer, o programa deve mostrar uma mensagem de sucesso e interromper o loop com break.'''

senha_correta = "python123"  # Definindo a senha correta

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido!")
        break  # Sai do loop
    else:
        print("Senha incorreta. Tente novamente.")
