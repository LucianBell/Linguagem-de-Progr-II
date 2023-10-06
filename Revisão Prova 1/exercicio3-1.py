
class CarroDeCorrida:
    def __init__(self, numeroCarro, piloto, equipe, velocidadeMaxima):
        self.__velocidadeMaxima = velocidadeMaxima
        self.__equipe = equipe
        self.__piloto = piloto
        self.__numeroCarro = numeroCarro
        self.__velocidadeAtual = 0.0
        self.__ligado = False

    def get_numeroCarro(self):
        print(f"Número do carro: {self.__numeroCarro}")

    def get_piloto(self):
        print(f"Piloto escalado: {self.__piloto}")

    def get_equipe(self):
        print(f"Equipe: {self.__equipe}")

    def get_velocidade(self):
        print(f"Velocidade máxima: {self.__velocidadeMaxima}")

    def get_ligado(self):
        if not self.__ligado:
            print("O carro está desligado")
        else:
            print("O carro está ligado")

    def get_veloAtual(self):
        print(f"Velocidade atual {self.__velocidadeAtual}")

    def aumentarVelocidade(self, aumento):
        if self.__ligado:
            if self.__velocidadeAtual + aumento > self.__velocidadeMaxima:
                self.__velocidadeAtual = self.__velocidadeMaxima
                print(f"Velocidade atual aumentada para {self.__velocidadeAtual}")
            else:
                self.__velocidadeAtual += aumento
                print(f"Velocidade atual aumentada para {self.__velocidadeAtual}")
        else:
            print("Carro só pode acelerar se estiver ligado")

    def frear(self, percent):
        if self.__ligado and self.__velocidadeAtual > 0.0:
            self.__velocidadeAtual = (self.__velocidadeAtual * (100 - percent)/100)
            print("Sucesso")
        else:
            print("Erro")

    def desligar(self):
        if self.__ligado == True and self.__velocidadeAtual == 0.0:
            self.__ligado = False
            print("Sucesso")
        else:
            print("Error")


if __name__ == '__main__':
    C1 = CarroDeCorrida(200, "John", "RedBull", 250)
    print(C1)