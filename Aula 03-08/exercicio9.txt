#Faça um programa que imprima a tabela ASCII (letra e código decimal correspondente).

i = 0

while i <= 127:
    print("Letra: ", chr(i))
    print("Valor ASCII: ", i)
    print("------------------")
    i += 1
