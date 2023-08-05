"""
Uma companhia telefônica opera com a seguinte tarifa: uma chamada telefônica com duração de 3 minutos
custa R$ 1.15. Cada minuto adicional custa R$ 0.26. Escreva um programa que leia a duração total de
uma chamada (em minutos) e calcule o total a ser pago.
"""

duracao = int(input("Escreva a duracao da chamada em minutos: "))

if duracao <= 3:
    print("Custo total: R$ 1.15")
else:
    custo = 1.15
    duracao -= 3
    while duracao > 0:
        custo += 0.26
        duracao -= 1
    print(f"Custo total: R${custo}")
