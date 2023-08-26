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
    def __init__(self, raio, centro_x, centro_y):
        self.raio = raio
        self.centro_x = centro_x
        self.centro_y = centro_y

    def __calcular_area(self):
        print(f"Área do círculo: {(self.raio * self.raio) * 3.14}")

    def __calcular_circunferencia(self):
        print(f"Área do círculo: {2 * 3.14 * self.raio}")

    def mostrar_calculos(self):
        self.__calcular_area()
        self.__calcular_circunferencia()

    def definir_raio(self, raio_novo):
        self.raio = raio_novo
        print(f"Raio atualizado: {self.raio}")

    def definir_aumento_raio(self, aumento_raio):
        aumento = 1 + (aumento_raio/100.0)
        self.raio = (self.raio * aumento)
        print(f"Novo raio: {self.raio}")

    def definir_centro(self, novo_x, novo_y):
        self.centro_x = novo_x
        self.centro_y = novo_y
        print("Novas coordenadas para o centro definidas")

    def mostrar_raio(self):
        print(f"Raio: {self.raio}")

    def mostrar_centro(self):
        print(f"Centro do círculo: x = {self.centro_x} y = {self.centro_y}")

    def mostrar_area_circulo(self):
        print(f"Área do círculo: {self.__calcular_area()}")


circuloTeste = Circulo(3.14, 0, 0)
circuloTeste.mostrar_calculos()
