"""
Crie uma classe chamada ContaInvestimento :
         class ContaInvestimeto(Conta):
                    pass
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def atualiza(self):
        pass


class ContaInvestimento(Conta):
    def __init__(self, saldo):
        self.saldo = saldo

    def atualiza(self):
        self.saldo += self.saldo
