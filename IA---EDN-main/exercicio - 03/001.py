'''1 - Crie um programa que solicite ao usuário uma nota (de 0 a 10) e exiba uma mensagem dizendo se o aluno foi reprovado, em recuperação ou aprovado.'''

nota = float(input("Digite a nota do aluno (0 a 10): "))

# Verifica a faixa da nota
if nota < 5:
    print("Reprovado.")
elif nota < 7:
    print("Recuperação.")
else:
    print("Aprovado.")
