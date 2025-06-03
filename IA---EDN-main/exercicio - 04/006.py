'''6 - Peça ao usuário que digite 10 números inteiros. Armazene apenas os números pares válidos em uma lista. Use try/except para capturar erros, continue para ignorar números ímpares ou inválidos, e exiba a lista final ao terminar.'''

def coletar_pares():
    pares = []
    tentativas = 0

    print("Digite 10 números inteiros. Somente os pares válidos serão armazenados.\n")

    while tentativas < 10:
        entrada = input(f"Digite o {tentativas + 1}º número: ")

        try:
            numero = int(entrada)
            tentativas += 1  # Conta como tentativa válida, mesmo se ímpar
            if numero % 2 == 0:
                pares.append(numero)
            else:
                print("⚠️ Número ímpar ignorado.\n")
                continue
        except ValueError:
            print("❌ Entrada inválida! Digite um número inteiro.\n")
            continue

    print("\n📋 Números pares válidos inseridos:")
    print(pares if pares else "Nenhum número par foi inserido.")

# Executa a função
coletar_pares()
