def calcular_media(nota1, nota2):
    # Cálculo da média
    media = (nota1 + nota2) / 2
    return media

# Entrada de dados
nota_primeira = float(input("Digite a primeira nota: "))
nota_segunda = float(input("Digite a segunda nota: "))

# Cálculo e exibição da média
media_final = calcular_media(nota_primeira, nota_segunda)
print("A média das duas notas é: ", media_final)