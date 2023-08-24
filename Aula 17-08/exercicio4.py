"""
Inclua, no modelo Lampada, uma operação estáLigada que retorne verdadeiro se a lâmpada estiver ligada e falso
, caso contrário.
"""

class Lampada:
    def __init__(self, marca, tipoDeLampada, temperaturaDaLampada, preco, voltagem, ligada):
        self.marca = marca
        self.tipoDeLampada = tipoDeLampada
        self.temperaturaDaLampada = temperaturaDaLampada
        self.preco = preco
        self.voltagem = voltagem
        self.ligada = ligada

    def mudarEstado(self):
        if self.ligada:
            self.ligada = False
            return "Desligando lampada..."
        else:
            self.ligada = True
            return "Ligando lampada..."

    def esta_ligada(self):
        if self.ligada:
            return True
        else:
            return False

    def mostrar_preco(self):
        return f"Preço da lampada: R$ {self.preco:.2f}"


lampadaTeste = Lampada(marca="teste", tipoDeLampada="LED", temperaturaDaLampada="branca", preco=10.00,
                       voltagem=220, ligada=False)

print(lampadaTeste.tipoDeLampada)
print(lampadaTeste.voltagem)
print(lampadaTeste.mostrar_preco())
print(lampadaTeste.esta_ligada())
print(lampadaTeste.mudarEstado())
print(lampadaTeste.esta_ligada())

