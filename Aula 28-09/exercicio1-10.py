"""
Implemente a seguinte estrutura de classes:

...
"""

from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def empresta(self):
        pass

    @abstractmethod
    def retorna(self):
        pass


class ItemRestrito(Item):
    @abstractmethod
    def alteraNivel(self):
        pass


class Livro(Item):
    def empresta(self):
        print("Livro emprestado")

    def retorna(self):
        print("Livro retornado")


class Periodico(Item):
    def empresta(self):
        print("Periódico emprestado")

    def retorna(self):
        print("Periódico retornado")


class Fita(ItemRestrito):
    def empresta(self):
        print("Fita emprestada")

    def retorna(self):
        print("Fita retornada")

    def alteraNivel(self):
        print("Nível da fita alterado")


class SalaEstudo(ItemRestrito):
    def empresta(self):
        print("Sala de estudo emprestada")

    def retorna(self):
        print("Sala de estudo retornada")

    def alteraNivel(self):
        print("Nível da sala de estudo alterado")


if __name__ == '__main__':
    livro = Livro()
    livro.empresta()
    livro.retorna()

    periodico = Periodico()
    periodico.empresta()
    periodico.retorna()

    fita = Fita()
    fita.empresta()
    fita.alteraNivel()
    fita.retorna()

    sala_estudo = SalaEstudo()
    sala_estudo.empresta()
    sala_estudo.alteraNivel()
    sala_estudo.retorna()
