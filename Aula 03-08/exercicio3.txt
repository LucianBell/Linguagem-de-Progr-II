#Faça um programa que leia um nº inteiro e mostre uma mensagem indicando se este número
#é par ou ímpar, e se é positivo ou negativo.

num = int(input("Insira um numero: "))

if num == 0:
    print("Zero")
elif num % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")

if num > 0:
    print("Numero positivo")
elif num == 0:
    print("Nem negativo, nem positivo")
else:
    print("Numero negativo")
