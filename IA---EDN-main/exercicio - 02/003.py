'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Função de conversão
def converter_temperatura(valor, origem, destino):
    if origem == destino:
        return valor

    # Converte para Celsius
    if origem == "F":
        valor = (valor - 32) * 5/9
    elif origem == "K":
        valor = valor - 273.15

    # Converte de Celsius para destino
    if destino == "F":
        return (valor * 9/5) + 32
    elif destino == "K":
        return valor + 273.15
    elif destino == "C":
        return valor

# Entrada do usuário
temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Validação e conversão
unidades_validas = {"C", "F", "K"}
if origem in unidades_validas and destino in unidades_validas:
    resultado = converter_temperatura(temp, origem, destino)
    print(f"{temp}°{origem} é igual a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida. Use C, F ou K.")
