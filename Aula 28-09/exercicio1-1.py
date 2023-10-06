"""
Torne a classe Conta abstrata.

import abc
class Conta(ABC):
          def __init__(self, numero, titular, saldo=0, limite=1000.0):
                 self._numero = numero
                 self._titular = titular
                 self._saldo = saldo
                 self._limite = limite

# outros métodos e propriedades
"""

import abc
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @abstractmethod
    def get_numer(self):
        pass

    def get_titular(self):
        pass

    def get_saldo(self):
        pass

    def get_limite(self):
        pass

