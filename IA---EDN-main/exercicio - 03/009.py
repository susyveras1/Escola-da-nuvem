'''9 - Crie um programa onde o computador escolhe um número entre 1 e 10, e o usuário deve adivinhar qual é. O programa continua até que o usuário acerte.'''

import random

numero_secreto = random.randint(1, 10)  # Número aleatório entre 1 e 10

while True:
    tentativa = int(input("Adivinhe o número entre 1 e 10: "))
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Tente novamente.")
