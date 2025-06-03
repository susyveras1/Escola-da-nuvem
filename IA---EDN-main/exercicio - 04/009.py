'''9 - Solicite ao usuário números inteiros até que ele digite "0". Armazene os positivos e negativos separadamente em duas listas. Ignore valores não inteiros com try/except. No final, mostre quantos positivos e negativos foram inseridos.'''

def separar_numeros():
    positivos = []
    negativos = []

    print("🔢 Digite números inteiros (digite 0 para encerrar).")
    print("Valores não inteiros serão ignorados.\n")

    while True:
        entrada = input("Digite um número inteiro: ")

        try:
            numero = int(entrada)
            if numero == 0:
                break
            elif numero > 0:
                positivos.append(numero)
            else:
                negativos.append(numero)
        except ValueError:
            print("❌ Entrada inválida! Digite um número inteiro.\n")
            continue

    print("\n📊 Resultados:")
    print(f"Positivos inseridos: {len(positivos)} → {positivos}")
    print(f"Negativos inseridos: {len(negativos)} → {negativos}")

# Executa a função
separar_numeros()
