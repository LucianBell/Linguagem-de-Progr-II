class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def caminha(self):
        print("caminhando...")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def late(self):
        print("Au au uWu")


class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def mia(self):
        print("Miau miau uWu")