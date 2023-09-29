"""
Implementente uma classe Carro que deve conter um metodo liga que imprime
"Carro ligado" e um atributo velocidade. Implemente tambem o construtor da classe.
"""


class Carro:
    def __init__(self, velocidade, ligado=False):
        self.ligado = ligado
        self.velocidade = velocidade

    def liga(self):
        if self.ligado == False:
            print("Carro ligado")
            self.ligado = True
        else:
            print("Carro desligado")
            self.ligado = False


if __name__ == '__main__':
    meu_carro = Carro(200)
    meu_carro.liga()
    print("-------------")
    meu_carro.liga()
