'''5 - Crie um programa que solicite ao usuário a idade de várias pessoas. Armazene apenas idades válidas (entre 0 e 120) em uma lista. Use for, try/except, continue para ignorar entradas inválidas, e break para encerrar o programa se o usuário digitar "fim". No final, exiba a lista das idades válidas.'''

def coletar_idades():
    idades_validas = []

    print("Digite a idade das pessoas. Para encerrar, digite 'fim'.")
    print("Somente idades entre 0 e 120 serão aceitas.\n")

    for _ in range(1000):  # Usamos um laço for com um limite grande, o break controlará a parada real
        entrada = input("Digite uma idade: ")

        if entrada.lower() == 'fim':
            break

        try:
            idade = int(entrada)
            if 0 <= idade <= 120:
                idades_validas.append(idade)
            else:
                print("❌ Idade fora do intervalo permitido (0 a 120). Ignorada.\n")
                continue
        except ValueError:
            print("❌ Entrada inválida! Digite um número inteiro ou 'fim' para sair.\n")
            continue

    print("\n📋 Idades válidas registradas:")
    print(idades_validas if idades_validas else "Nenhuma idade válida foi inserida.")

# Executa a função
coletar_idades()
