"""
Crie um modelo Ponto2D para representar um ponto no espaço cartesiano de duas dimensões.
Que dados e operações esse modelo deve ter? Dica: Imagine um gráfico no qual você tenha que desenhar pontos,
baseados nesse modelo.
"""
import math


class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, outro_ponto):
        dx = self.x - outro_ponto.x
        dy = self.y - outro_ponto.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia

    def mostrar_coordenadas(self):
        print(f"Coordenadas: ({self.x}, {self.y})")


ponto1 = Ponto2D(3, 4)
ponto2 = Ponto2D(-1, 2)

ponto1.mostrar_coordenadas()
ponto2.mostrar_coordenadas()

distancia_entre_pontos = ponto1.calcular_distancia(ponto2)
print(f"A distância entre os pontos é: {distancia_entre_pontos}")
