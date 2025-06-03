'''8 - Crie um programa que solicita a nota de avaliação de um restaurante (de 0 a 5) e exibe a quantidade de estrelas equivalente, com mensagem personalizada.'''

nota = int(input("Avalie o restaurante de 0 a 5 estrelas: "))

if nota == 5:
    print("★★★★★ - Excelente!")
elif nota == 4:
    print("★★★★ - Muito bom!")
elif nota == 3:
    print("★★★ - Bom.")
elif nota == 2:
    print("★★ - Regular.")
elif nota == 1:
    print("★ - Ruim.")
elif nota == 0:
    print("Sem estrelas - Péssimo.")
else:
    print("Nota inválida. Use valores de 0 a 5.")
