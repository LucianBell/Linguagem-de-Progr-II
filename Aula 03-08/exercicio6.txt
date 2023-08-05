"""
O cardápio de uma lancheria é o seguinte:

Especificação	Código	Preço
Cachorro quente	100	    1,20
Bauru simples	101	    1,30
Bauru com ovo	102	    1,50
Hambúrger	    103	    1,20
Cheeseburguer	104	    1,30
Refrigerante	105	    1,00

Escrever um algoritmo que leia o código
do item pedido, a quantidade e calcule
o valor a ser pago por aquele lanche.
Considere que será lido o código de um único item.
"""

codigo = int(input("Insira o codigo do produto: "))
if codigo < 100 or codigo > 105:
    print("Codigo invalido")
else:
    quantidade = float(input("Insira a quantidade do produto: "))
    if codigo == 100:
        print("Valor do pedido: ", 1.20 * quantidade)
    elif codigo == 101:
        print("Valor do pedido: ", 1.30 * quantidade)
    elif codigo == 102:
        print("Valor do pedido: ", 1.50 * quantidade)
    elif codigo == 103:
        print("Valor do pedido: ", 1.20 * quantidade)
    elif codigo == 104:
        print("Valor do pedido: ", 1.30 * quantidade)
    elif codigo == 105:
        print("Valor do pedido: ", 1.00 * quantidade)
