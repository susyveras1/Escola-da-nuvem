'''8 - Crie um programa para registrar as temperaturas de vários dias. O usuário deve digitar a temperatura em graus Celsius (ex: 25.5). O programa continua coletando até que o usuário digite "fim" ou colete 7 temperaturas. Valores inválidos devem ser ignorados. Ao final, exiba a média das temperaturas registradas.'''

def registrar_temperaturas():
    temperaturas = []

    print("🌡️ Registro de Temperaturas (até 7 dias)")
    print("Digite 'fim' para encerrar a qualquer momento.\n")

    while len(temperaturas) < 7:
        entrada = input(f"Digite a temperatura do dia {len(temperaturas) + 1} (em °C): ")

        if entrada.lower() == "fim":
            break

        try:
            temp = float(entrada)
            temperaturas.append(temp)
        except ValueError:
            print("❌ Valor inválido! Digite um número como 25.5 ou 'fim' para sair.\n")
            continue

    print("\n📋 Temperaturas registradas:")
    print(temperaturas if temperaturas else "Nenhuma temperatura registrada.")

    if temperaturas:
        media = sum(temperaturas) / len(temperaturas)
        print(f"📈 Média das temperaturas: {media:.2f} °C")
    else:
        print("⚠️ Não foi possível calcular a média.")

# Executa a função
registrar_temperaturas()
