"""
Faça a mesma coisa que o exercicio anterior (crei uma classe CarroAnfibio2). Porém inverta a ordem da herança,
herde primeiro Barco e depois Carro. Instancie um objeto dessa classe e invoque o metodo liga. Observe qual a
saída do código.
"""

from exercicio1 import Carro
from exercicio2 import Barco


class CarroAnfibio(Barco, Carro):
    def liga(self):
        super().__init__(self.velocidade, self.ligado)
        print("Ligando carro anfibio")


if __name__ == '__main__':
    meu_ca = CarroAnfibio(200)
    meu_ca.liga()
    print("Velocidade do Carro Anfibio: ", meu_ca.velocidade, "km/h")
