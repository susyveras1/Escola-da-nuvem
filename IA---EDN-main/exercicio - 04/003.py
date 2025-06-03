'''3 - Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''

def senha_forte():
    print("Verificador de Senha Forte")
    print("A senha deve ter pelo menos 8 caracteres e conter ao menos 1 número.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        senha = input("Digite uma senha: ")

        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break

        if len(senha) < 8:
            print("❌ A senha deve ter no mínimo 8 caracteres.\n")
            continue

        if not any(char.isdigit() for char in senha):
            print("❌ A senha deve conter pelo menos um número.\n")
            continue

        print("✅ Senha forte! Programa encerrado.")
        break

# Executa a função
senha_forte()
