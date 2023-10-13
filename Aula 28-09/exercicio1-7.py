"""
Não conseguimos instanciar uma ContaInvestimento que herda Conta sem implementar o método abstrato atualiza().
Vamos criar uma implementação dentro da classe

ContaInvestimento :
          def atualiza(self, taxa):
                      self._saldo += self._saldo * taxa * 5
"""

from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def atualiza(self, taxa):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa


class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5


if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)
    ci = ContaInvestimento('123-6', 'Maria', 1000.0)
    ci.atualiza(0.01)
    print(ci.saldo)

    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(cc.saldo)
    print(cp.saldo)
