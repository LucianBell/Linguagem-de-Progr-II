"""
Implemente uma classe Barco que deve conter um metodo liga que imprime "Barco ligado"
e um atributo velocidade. Implemente tambem o construtor da classe.
"""


class Barco:
    def __init__(self, velocidade, ligado=False):
        self.ligado = ligado
        self.velocidade = velocidade

    def liga(self):
        if not self.ligado:
            print("Carro ligado")
            self.ligado = True
        else:
            print("Carro desligado")
            self.ligado = False


if __name__ == '__main__':
    meu_barco = Barco(200)
    meu_barco.liga()
    print("Velocidade do barco: ", meu_barco.velocidade, "km/h")
    print("-------------")
    meu_barco.liga()
