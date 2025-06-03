'''6- Calculadora de Média Escolar
Enunciado:
Desenvolva um programa que solicite o nome de um aluno e suas 3 notas. O programa deve calcular a média e informar se o aluno foi aprovado (média >= 7), está em recuperação (5 <= média < 7) ou foi reprovado (média < 5).'''


# Solicita o nome e as 3 notas ao usuário
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica a situação do aluno
if media >= 7:
    situacao = "Aprovado"
elif 5 <= media < 7:
    situacao = "Em recuperação"
else:
    situacao = "Reprovado"

# Exibe o resultado
print(f"\nNome: {nome}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
