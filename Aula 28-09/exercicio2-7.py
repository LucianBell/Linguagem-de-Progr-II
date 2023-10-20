"""
Crie um programa que leia um data fornecida por um usuário (dia, mes e ano - podem ser lidos separadamente).
A função deverá disparar uma exceção se o dia, mes ou ano fornecido for inválido informando uma mensagem
de erro ao usuário
"""


class DataInvalidaException(Exception):
    pass


def verificar_data(dia, mes, ano):
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
        raise DataInvalidaException("Data inválida. Verifique o dia, mês e ano.")


def ler_data():
    try:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))

        verificar_data(dia, mes, ano)

        print("Data válida:", dia, "/", mes, "/", ano)

    except ValueError:
        print("Erro: Os valores informados devem ser números inteiros.")
    except DataInvalidaException as e:
        print("Erro:", e)


if __name__ == "__main__":
    ler_data()