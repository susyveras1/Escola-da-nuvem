'''7 - Crie um programa que permita que o usuário monte uma lista de compras digitando nomes de produtos. O usuário pode digitar até 10 itens. Se digitar "fim", o programa para imediatamente (break). Se o item for vazio (só apertar Enter), ele é ignorado com continue. Use try/except para garantir que apenas strings sejam inseridas.'''

def lista_de_compras():
    compras = []

    print("🛒 Monte sua lista de compras (até 10 itens).")
    print("Digite 'fim' para encerrar a qualquer momento.\n")

    for i in range(10):
        try:
            item = input(f"Produto {i + 1}: ")

            if item.lower() == 'fim':
                break

            if item.strip() == '':
                print("⚠️ Entrada vazia ignorada.\n")
                continue

            # Aqui garantimos que o item seja uma string (input já retorna string, mas tratamos para robustez)
            if not isinstance(item, str):
                raise ValueError("Entrada inválida. Esperado um texto.")
            
            compras.append(item)
        except Exception as erro:
            print(f"❌ Erro: {erro}\n")
            continue

    print("\n📋 Sua lista de compras:")
    if compras:
        for i, produto in enumerate(compras, 1):
            print(f"{i}. {produto}")
    else:
        print("Nenhum item foi adicionado.")

# Executa a função
lista_de_compras()
