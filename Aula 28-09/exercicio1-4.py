"""
Defina o código necessário para que você consiga instanciar uma ContaCorrente e uma ContaPoupanca da seguinte forma:

if __name__ == '__main__':
            cc = ContaCorrente('123-4', 'João', 1000.0)
            cp = ContaPoupanca('123-5', 'José', 1000.0)

             cc.atualiza(0.01)
             cp.atualiza(0.01)
             print(cc.saldo)
             print(cp.saldo)



*** ContaCorrente e ContaPoupanca são derivadas da classe abstrata Conta
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


if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)

    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(cc.saldo)
    print(cp.saldo)