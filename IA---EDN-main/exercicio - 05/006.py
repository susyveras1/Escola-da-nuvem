'''6 - Crie um programa que peça ao usuário o nome e a idade. Em seguida, exiba uma mensagem personalizada com o nome e a idade da pessoa. Toda a lógica deve estar dentro de uma função main(), e o programa deve ser executado com if __name__ == "__main__":.'''

def main():
    try:
        nome = input("Digite seu nome: ").strip()
        idade = int(input("Digite sua idade: "))
        print(f"Olá, {nome}! Você tem {idade} anos.")
    except ValueError:
        print("Erro: A idade deve ser um número inteiro.")

# Executa o programa apenas se for o arquivo principal
if __name__ == "__main__":
    main()
