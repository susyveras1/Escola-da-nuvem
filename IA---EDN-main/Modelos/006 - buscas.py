# Algoritmo de busca

def busca (Lista, nome_procurado):
    for i in range(len(Lista)):
        if Lista[i] == nome_procurado:
            return i + 1
    return -1 

nomes = ['Geovanna', 'Ingryd', 'Alberto', 'Iolanda', 'Maria', 'Jackson', 'Evelyn', 'Janaina', 'Wellington', 'Gustavo', 'Ana', 'Marcos', 'Vinicius', 'Vanessa', 'Thauan', 'Ricardo', 'Regina', 'Ramon', 'Rafael', 'Núbia', 'Mirela', 'Maria Eduarda', 'Kamily', 'José', 'João', 'João Lucas', 'João Henrique', 'Andrei', 'Ana', ]
nome_procurado = input('Qual nome você quer procurar? ')
posicao = busca(nomes, nome_procurado)
if posicao != -1:
    print('O nome está na posição', posicao)
else:
    print('O nome não está na lista')

# Algoritmo de busca - Binario

def binaria (lista, valor_procurado):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor_procurado:
            return meio + 1
        elif lista[meio] < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

numeros = [0, 2, 4, 6, 8, 10]
valor_procurado = int(input('Qual o valor você quer procurar? '))
posicao = binaria(numeros, valor_procurado)
if posicao != -1:
    print('O valor está na posição', posicao)
else:
    print('O valor não está na lista')