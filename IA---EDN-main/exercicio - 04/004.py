'''4 - Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.'''

def registrar_notas():
    notas = []

    print("Registro de Notas da Turma")
    print("Digite 'fim' para encerrar.")
    print("Notas válidas: de 0 a 10.\n")

    while True:
        entrada = input("Digite a nota do aluno: ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("❌ Nota inválida! Digite um valor entre 0 e 10.\n")
        except ValueError:
            print("❌ Entrada inválida! Digite um número ou 'fim' para encerrar.\n")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\n✅ Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# Executa a função
registrar_notas()
