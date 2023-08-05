"""
Elabore um programa que dada a idade de um nadador classifica-o em uma das seguintes categorias:

- infantil A = 5 - 7 anos
- infantil B = 8-10 anos
- juvenil A = 11-13 anos
- juvenil B = 14-17 anos
- adulto = maiores de 18 anos
"""

idadeNadador = int(input("Insira a idade do nadador: "))

if idadeNadador < 5:
    print("Nadador não tem idade para se classificar")
elif idadeNadador <= 7:
    print("Nadador classificado na categoria infantil A")
elif idadeNadador <= 10:
    print("Nadador classificado na categoria infantil B")
elif idadeNadador <= 13:
    print("Nadador classificado na categoria juvenil A")
elif idadeNadador <= 17:
    print("Nadador classificado na categoria juvenil B")
else:
    print("Nadador classificado na categoria adulto")
