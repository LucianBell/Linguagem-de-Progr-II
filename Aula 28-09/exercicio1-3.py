"""
Tente instânciar uma Conta :

if __name__ == '__main__':
          c = Conta()

O que acontece? Por que?
"""

from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def atualiza(self):
        pass


if __name__ == '__main__':
    c = Conta()

"""
Acontece um erro. Isso acontece porque uma classe abstrata é uma classe que não pode ser instanciada diretamente.
Ela é projetada para ser uma classe base para outras classes e contém métodos abstratos, que são declarados mas
não são implementados na classe abstrata.
"""
