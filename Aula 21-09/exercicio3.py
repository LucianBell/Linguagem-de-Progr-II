"""
Agora implemente uma classe CarroAnfibio é subclasse de Carro e Barco implementados anteriormente.

Essa classe deve ter um metodo liga que invoca o construtor super(). Instancie um objeto dessa
classe e invoque o metodo liga. Observe qual a saída do código.
"""

from exercicio1 import Carro
from exercicio2 import Barco


class CarroAnfibio(Carro, Barco):
    def liga(self):
        super().__init__(self.velocidade, self.ligado)
        print("Ligando carro anfibio")


if __name__ == '__main__':
    meu_ca = CarroAnfibio(200)
    meu_ca.liga()
    print("Velocidade do Carro Anfibio: ", meu_ca.velocidade, "km/h")
