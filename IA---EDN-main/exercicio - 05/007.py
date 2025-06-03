'''7 - Crie um programa que permita ao usuário montar uma lista de compras. O usuário poderá adicionar itens até digitar "fim". Ao final, o programa exibirá todos os itens da lista. O programa deve estar estruturado com uma função main() e ser executado com if __name__ == "__main__":.'''

def main():
    lista_compras = []

    print("=== Lista de Compras ===")
    print("Digite os itens um por um. Digite 'fim' para encerrar.\n")

    while True:
        item = input("Adicionar item: ").strip()
        if item.lower() == "fim":
            break
        elif item == "":
            print("Você não digitou nenhum item.")
        else:
            lista_compras.append(item)

    print("\nItens da sua lista de compras:")
    for i, item in enumerate(lista_compras, 1):
        print(f"{i}. {item}")

# Executa o programa apenas se for o arquivo principal
if __name__ == "__main__":
    main()
