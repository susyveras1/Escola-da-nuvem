''' 4 - Crie uma função que recebe dois números e retorna a soma. O programa deve pedir os números ao usuário, chamar a função e exibir o resultado.'''

# Função que retorna a soma de dois números
def somar(numero1, numero2):
    return numero1 + numero2

# Programa principal
def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        resultado = somar(num1, num2)
        print(f"A soma de {num1} e {num2} é: {resultado}")
    
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

# Executa o programa
main()
