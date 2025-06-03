'''1 - Crie uma função que receba uma lista de notas (valores float) e calcule a média. O programa principal deverá solicitar ao usuário o nome de um aluno e suas 3 notas, e então utilizar a função para calcular e exibir a média com duas casas decimais.'''

# Função que calcula a média de uma lista de notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Programa principal
def main():
    nome = input("Digite o nome do aluno: ")
    
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    
    print(f"A média de {nome} é: {media:.2f}")

# Executa o programa
main()
