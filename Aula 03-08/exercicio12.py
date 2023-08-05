"""
Faça um programa que converta graus Co em graus Fo e vice-versa. Ou seja, se for lida uma temperatura
em graus Celsius, esta deverá ser convertida em graus Fahrenheit e se for lida em graus Fahrenheit,
deverá ser convertida em graus Celsius.
"""


def paraFahrenheit(temp_celsius):
    fahrenheit = (9 / 5) * temp_celsius + 32
    return fahrenheit

def paraCelsius(temp_fahrenheit):
    celsius = (5 / 9) * (temp_fahrenheit - 32)
    return celsius

print("Menu de alternativas:")
print("1 - Converter de fahrenheit para celsius")
print("2 - Converter de celsius para fahrenheit")

escolha = int(input())

if escolha < 1 or escolha > 2:
    print("Escolha invalida")
elif escolha == 1:
    temp = int(input("Insira a temperatura:"))
    celsius = paraCelsius(temp)
    print("Temperatura em celsius: ", celsius)
else:
    temp = int(input("Insira a temperatura:"))
    fahrenheit = paraFahrenheit(temp)
    print("Temperatura em fahrenheit: ", fahrenheit)
