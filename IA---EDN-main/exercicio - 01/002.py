# 002 - Crie um programa em Python que solicite um número do usuário e informe se ele é par ou ímpar.

# Solicita um número do usuário
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    '''
    Verifica se o número é par. 
    O operador % (módulo) retorna o resto da divisão de 'numero' por 2.
    Se o resto for 0, significa que 'numero' é divisível por 2, ou seja, é um número par.
     '''
    
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


