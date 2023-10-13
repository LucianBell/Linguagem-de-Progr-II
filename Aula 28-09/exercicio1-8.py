"""
Agora teste instanciando uma ContaInvestimento e chame o método atualiza()

ci = ContaInvestimento('123-6', 'Maria', 1000)
ci.deposita(1000.0)
ci.atualiza(0.01)
print(ci.saldo)
"""


class Conta:
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def mostra_saldo(self):
        return self.__saldo


class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa * 5


if __name__ == '__main__':
    ci = ContaInvestimento('123-6', 'Maria', 1000)
    ci.deposita(1000.0)
    ci.atualiza(0.01)
    print(ci.mostra_saldo())
