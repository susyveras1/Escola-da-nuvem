'''5 - Crie um programa com uma função que cadastre alunos e suas respectivas notas.
O sistema deve:
Solicitar o nome do aluno.
Solicitar 3 notas válidas (entre 0 e 10).
Armazenar os dados em um dicionário, onde a chave é o nome e o valor é uma lista de notas.
Permitir o cadastro de vários alunos até que o usuário digite "fim".
Exibir ao final:
A lista de alunos e suas médias.
O aluno com a maior média.
Use def para as funcionalidades e try/except para tratar entradas inválidas.'''

# Função para solicitar uma nota válida entre 0 e 10
def obter_nota_valida(indice):
    while True:
        try:
            nota = float(input(f"Digite a {indice}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Digite um número válido.")

# Função para cadastrar alunos
def cadastrar_alunos():
    alunos = {}

    while True:
        nome = input("\nDigite o nome do aluno (ou 'fim' para encerrar): ").strip()
        if nome.lower() == "fim":
            break
        
        notas = []
        for i in range(1, 4):
            nota = obter_nota_valida(i)
            notas.append(nota)
        
        alunos[nome] = notas
    return alunos

# Função para calcular e exibir resultados
def exibir_resultados(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\nMédias dos alunos:")
    maior_media = -1
    melhor_aluno = ""

    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        print(f"{nome}: média = {media:.2f}")
        if media > maior_media:
            maior_media = media
            melhor_aluno = nome
    
    print(f"\nAluno com a maior média: {melhor_aluno} ({maior_media:.2f})")

# Programa principal
def main():
    print("=== Cadastro de Alunos ===")
    alunos_cadastrados = cadastrar_alunos()
    exibir_resultados(alunos_cadastrados)

# Executa o programa
main()
