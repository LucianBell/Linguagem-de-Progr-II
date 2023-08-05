#Uma firma contrata um encanador a R$ 20,00 por dia. Escreva um programa que leia o número
# de dias trabalhados pelo encanador e imprima a quantia liquida que deverá ser paga,
# sabendo-se que são descontados 8% para o imposto de renda.

dias = int(input("Numero de dias trabalhados pelo encanador: "))
pagamento = (((dias * 20.00) * 92) / 100)

print(f"Valor liquido que devera ser pago R$ {pagamento}")
