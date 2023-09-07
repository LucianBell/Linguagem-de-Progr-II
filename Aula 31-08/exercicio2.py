"""
Utilize a classe CarrodeCorrida criada anteriormente efetue as seguintes ações:

Instancie um objeto CarrodeCorrida
Mostre o nome do piloto, o nome da equipe e a velocidade máxima
Altere a velocidade máxima para 100 Km/h
Ligue o carro
Tente acelerar o carro a 120 Km/h  (lembre-se que o carro não pode exceder a velocidade máxima)
Acelere o carro a 90 km/h
Mostre a velocidade atual
Freie o carro 10%
Mostre a velocidade atual
Tente desligar o carro  (lembre-se que o carro não pode ser desligado sem parar....)
Pare o carro
Desligue o carro
"""


class CarroDeCorrida:
    def __init__(self, numero_carro, piloto, equipe, velocidade_maxima, velocidade_atual, ligado):
        self.numero_carro = numero_carro
        self.piloto = piloto
        self.equipe = equipe
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = velocidade_atual or 0
        self.ligado = ligado or False

    def setNumeroCarro(self, numeroCarro):
        self.numeroCarro = numeroCarro

    def setPiloto(self, piloto):
        self.piloto = piloto

    def setEquipe(self, equipe):
        self.equipe = equipe

    def setVelocidadeMaxima(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima

    def getNumeroCarro(self):
        return self.numeroCarro

    def getPiloto(self):
        return self.piloto

    def getEquipe(self):
        return self.equipe

    def getVelocidadeMaxima(self):
        return self.velocidade_maxima

    def getVelocidadeAtual(self):
        return self.velocidade_atual

    def isLigado(self):
        return self.ligado

    def acelerar(self, aumento):
        if self.ligado:
            self.velocidade_atual += aumento
            if self.velocidade_atual > self.velocidade_maxima:
                self.velocidade_atual = self.velocidade_maxima

    def frear(self, percentual):
        if self.ligado:
            self.velocidade_atual *= (1 - percentual / 100)
            if self.velocidade_atual < 0:
                self.velocidade_atual = 0

    def parar(self):
        self.velocidade_atual = 0

    def ligar(self):
        if not self.ligado and self.velocidade_atual == 0:
            self.ligado = True

    def desligar(self):
        if self.ligado and self.velocidade_atual == 0:
            self.ligado = False


if __name__ == '__main__':
    meu_carro = CarroDeCorrida(numero_carro=1, piloto="João", equipe="Equipe A", velocidade_maxima=80, ligado = False, velocidade_atual=0)

    print(
        f"Piloto: {meu_carro.getPiloto()}, Equipe: {meu_carro.getEquipe()}, "
        f"Velocidade Máxima: {meu_carro.getVelocidadeMaxima()} Km/h")

    meu_carro.setVelocidadeMaxima(100)

    meu_carro.ligar()

    meu_carro.acelerar(120)

    meu_carro.acelerar(90)

    print(f"Velocidade Atual: {meu_carro.getVelocidadeAtual()} Km/h")

    meu_carro.frear(10)

    print(f"Velocidade Atual após frear: {meu_carro.getVelocidadeAtual()} Km/h")

    meu_carro.desligar()

    meu_carro.parar()

    meu_carro.desligar()
