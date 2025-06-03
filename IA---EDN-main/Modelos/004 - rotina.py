# Sequência

print("acordei")
print("tomar agua")
print("ir ao banheiro")
print("ir pra escola")
print("estudar")
print("AWS")

#Definição clara
# Passo 1: pedir ao usuario pra inserir 2 numeros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Passo 2: fazer a soma dos números
soma = num1 + num2

# Passo 3: exibir o resultado
print("A soma dos números é:", soma)

# Finitude
'''for i in range(10):
    print("Numeros: ", i)
    if i == 5:
        break

while True:
    print("Não tem fim")'''
    

# determinismo
def soma(num1, num2):
    return num1 + num2

print(soma(6, 8))

