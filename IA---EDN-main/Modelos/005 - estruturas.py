# Estrutura sequencial

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
cidade = input('Qual a sua cidade? ')

print(f'Olá {nome}, você tem {idade} anos e mora em {cidade}.')

# Estrutura de repetição

for i in range(5):
    print("Numeros: ", i)

contar = 0
while contar < 5:
    print("Executar:" , contar)
    contar += 1
  
# Estrutura condicional

idade = int(input('Qual a sua idade? '))
if idade >= 18:
    print("Maior de idade")
elif idade <= 18:
    print("Menor de idade")
else:
    print("Idade inválida")

