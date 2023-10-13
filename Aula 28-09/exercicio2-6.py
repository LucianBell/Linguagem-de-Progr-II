"""
Crie um programa que leia um valor. Se o valor lido for um caracter deverá ser disparada uma exceção informando que o programa somente aceita valores inteiros. Se o valor lido for um inteiro,  deverá ser efetuada a seguinte análise baseada em faixas:
– Menor ou igual a 0 (zero): disparar uma exceção com a mensagem ValorAbaixoException
– Maior que 100 e menor que 1000 : disparar uma exceção com a mensagem ValorAltoException
– Maior ou igual a 1000: disparar uma exceção com a mensagem ValorMuitoAltoException
"""


class ValorAbaixoException(Exception):
    pass


class ValorAltoException(Exception):
    pass


class ValorMuitoAltoException(Exception):
    pass


def analisar_valor():
    try:
        valor = input("Digite um valor: ")
        if not valor.isdigit():
            raise ValueError("O valor deve ser um número inteiro.")

        valor = int(valor)

        if valor <= 0:
            raise ValorAbaixoException("ValorAbaixoException: O valor é menor ou igual a zero.")
        elif 100 < valor < 1000:
            raise ValorAltoException("ValorAltoException: O valor está entre 100 e 1000 (exclusive).")
        elif valor >= 1000:
            raise ValorMuitoAltoException("ValorMuitoAltoException: O valor é maior ou igual a 1000.")

        print("O valor está dentro da faixa desejada:", valor)

    except ValueError as ve:
        print("Erro:", ve)
    except ValorAbaixoException as vae:
        print("Erro:", vae)
    except ValorAltoException as vae:
        print("Erro:", vae)
    except ValorMuitoAltoException as vmae:
        print("Erro:", vmae)


if __name__ == "__main__":
    analisar_valor()
