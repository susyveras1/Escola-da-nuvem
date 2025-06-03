'''10 - Peça ao usuário para digitar palavras. Armazene apenas as palavras com mais de 5 letras em uma lista. Se a palavra for "parar", o programa encerra (break). Se a palavra for numérica (como "123"), ignore com continue. Use try/except para garantir que só palavras (strings) sejam processadas. No final, exiba a lista das palavras longas inseridas.'''

def coletar_palavras_longas():
    palavras_longas = []

    print("🔤 Digite palavras (somente com letras).")
    print("Digite 'parar' para encerrar o programa.\n")

    while True:
        try:
            entrada = input("Digite uma palavra: ")

            if entrada.lower() == "parar":
                break

            if entrada.isnumeric():
                print("⚠️ Palavras numéricas ignoradas.\n")
                continue

            if len(entrada) > 5:
                palavras_longas.append(entrada)
        except Exception as erro:
            print(f"❌ Erro inesperado: {erro}\n")
            continue

    print("\n📋 Palavras com mais de 5 letras:")
    if palavras_longas:
        for i, palavra in enumerate(palavras_longas, 1):
            print(f"{i}. {palavra}")
    else:
        print("Nenhuma palavra longa foi inserida.")

# Executa a função
coletar_palavras_longas()
