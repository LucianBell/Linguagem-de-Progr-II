"""
Imagine uma lâmpada que possa ter três estados: apagada, acesa e meia-luz. Escreva o modelo (classe)
LampadaTresEstados
"""


class LampadaTresEstados:
    def __init__(self, estado="apagada"):
        self.estado = estado

    def mostrarEstadoAtual(self):
        return f"Estado atual: {self.estado}"

    def acender(self):
        self.estado = "ligada"
        return f"Ligando lampada..."

    def desligar(self):
        self.estado = "desligada"
        return f"Desligando lampada..."

    def meia_luz(self):
        self.estado = "meia-luz"
        return f"Colocando lampada em meia-luz..."


lampadaTeste = LampadaTresEstados()

print(lampadaTeste.mostrarEstadoAtual())
print(lampadaTeste.acender())
print(lampadaTeste.desligar())
print(lampadaTeste.meia_luz())
