"""
Generalize o modelo LampadaTresEstados para que ele possa representar uma lâmpada onde a luminosidade pode ser
ajustada com qualquer valor entre 0% (apagada) e 100% (acesa). Dica: em vez de operações para possibilitar o
ajuste para cada um dos estados, descreva uma operação que receba um valor de ajuste.
"""


class LampadaTresEstados:
    def __init__(self, estado=0):
        self.estado = estado

    def mostrar_estado_atual(self):
        return f"Estado atual: {self.estado}% de intensidade"

    def mudar_estado(self, estado):
        if estado < 0 or estado > 100:
            return "Estado inválido. Intensidade deve estar entre 0% e 100%."
        else:
            self.estado = estado
            return f"Mudando estado para intensidade de luz {self.estado}%"


lampadaTeste = LampadaTresEstados()

print(lampadaTeste.mostrar_estado_atual())
print(lampadaTeste.mudar_estado(10))
print(lampadaTeste.mudar_estado(-10))
print(lampadaTeste.mudar_estado(90))