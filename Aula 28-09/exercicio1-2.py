"""
Torne o método atualiza() abstrato:

class Conta(ABC):
           def atualiza():
                     pass
"""

from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def atualiza(self):
        pass


class ContaPoupanca(Conta):
    def atualiza(self):
        return "Taxa de atualização da Conta Poupança aplicada!"


if __name__ == '__main__':
    conta_poupanca = ContaPoupanca()
    print(conta_poupanca.atualiza())