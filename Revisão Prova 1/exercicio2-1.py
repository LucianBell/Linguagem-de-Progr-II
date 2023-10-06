"""
Definir uma classe que represente um círculo.
Criar métodos Privados para:
1. calcular a área do círculo;
2. calcular a circunferência do círculo.
Criar métodos Públicos para:
1. definir o raio do círculo, dado um número real;
2. aumentar o raio do círculo, dado um percentual de aumento;
3. definir o centro do círculo, dada uma posição (X,Y);
4. imprimir o valor do raio;
5. imprimir o centro do círculo.
6. imprimir a área do círculo.
Criar um programa principal para testar a classe.
"""


class Circulo:
    def __init__(self, x_central, y_central, raio):
        self.__x_central = x_central
        self.__y_central = y_central
        self.__raio = raio

    def __calcular_area(self):
        area = 3.14 * (self.__raio * self.__raio)
        return area

    def __calcular_circunferencia(self):
        circunferencia = (self.__raio * 2) * 3.14
        return  circunferencia

    def set_raio(self, novo_raio):
        self.__raio = novo_raio

    def set_raio_percentual(self, percentual):
        self.__raio = (self.__raio * (1 + (percentual/100)))

    def set_posicao_central(self, novo_x, novo_y):
        self.__x_central = novo_x
        self.__y_central = novo_y

    def get_raio(self):
        print(f"Raio: {self.__raio}")

    def get_centro(self):
        print(f"Centro -> X: {self.__x_central} Y: {self.__y_central}")

    def get_area(self):
        print(f"Área do círculo: {self.__calcular_area()}")


if __name__ == '__main__':
    c1 = Circulo(1, 2, 3)

    c1.get_centro()
    c1.get_raio()
    c1.get_area()
