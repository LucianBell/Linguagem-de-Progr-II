"""
Crie a seguinte classe CarrodeCorrida

*Atributos:
- numeroCarro : int
- piloto : String
- equipe : String
- velocidadeMaxima : float
- velocidadeAtual : float
- ligado : boolean

*Métodos:
+ CarroCorrida(int numeroCarro, String piloto, String equipe, float velocidadeMaxima) - "Construtor"
+ set... (alterar atributos da Classe - "Modificadores")
+ get... (retorna valores dos atributos da Classe - "Acessores")
+ acelerar(float) - aumenta unidades em Km/h
+ frear(float) - reduz a velocidade em percentual (%) de frenagem
+ parar()
+ ligar()
+ desligar()

*Observações:
* Não utilize @property. Use setters e getters
*Não ultrapassar a velocidade máxima
*Frear e Acelerar só funcionam se o carro estiver ligado
*Desligar só funciona se o carro estiver parado
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

    def setVelocidadeMaxima(self, velocidadeMaxima):
        self.velocidadeMaxima = velocidadeMaxima

    def getNumeroCarro(self):
        return self.numeroCarro

    def getPiloto(self):
        return self.piloto

    def getEquipe(self):
        return self.equipe

    def getVelocidadeMaxima(self):
        return self.velocidadeMaxima

    def getVelocidadeAtual(self):
        return self.velocidadeAtual

    def isLigado(self):
        return self.ligado

    def acelerar(self, aumento):
        if self.ligado:
            self.velocidadeAtual += aumento
            if self.velocidadeAtual > self.velocidadeMaxima:
                self.velocidadeAtual = self.velocidadeMaxima

    def frear(self, percentual):
        if self.ligado:
            self.velocidadeAtual *= (1 - percentual / 100)
            if self.velocidadeAtual < 0:
                self.velocidadeAtual = 0

    def parar(self):
        self.velocidadeAtual = 0

    def ligar(self):
        if not self.ligado and self.velocidadeAtual == 0:
            self.ligado = True

    def desligar(self):
        if self.ligado and self.velocidadeAtual == 0:
            self.ligado = False
