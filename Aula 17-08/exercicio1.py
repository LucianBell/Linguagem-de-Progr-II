"""
Escreva um modelo para representar uma lâmpada que está à venda em um supermercado.
Que atributos devem ser representados por este modelo?
"""

"""
    def: Isso define uma função chamada __init__, que é o construtor da classe.
__init__ é uma função especial em Python que é usada dentro de uma classe para criar objetos dessa classe.
Quando você cria um objeto, o __init__ é executado automaticamente e define as características (atributos)
desse objeto.
"""

"""
self: É uma convenção em Python para referenciar a própria instância da classe. Ele é um parâmetro 
obrigatório em todos os métodos de instância da classe, incluindo o construtor. Ele permite que você
acesse e modifique os atributos da instância dentro do método.   
"""


class Lampada:
    def __init__(self, marca, tipoDeLampada, temperaturaDaLampada, cor, preco, voltagem, ligada):
        self.marca = marca
        self.tipoDeLampada = tipoDeLampada
        self.temperaturaDaLampada = temperaturaDaLampada
        self.cor = cor
        self.preco = preco
        self.voltagem = voltagem
        self.ligada = ligada

    def acende(self):
        if self.ligada:
            return "Desligando lampada..."
        else:
            return "Ligando lampada..."

    def mostrar_preco(self):
        return f"Preço da lampada: R$ {self.preco:.2f}"



lampadaTeste = Lampada(marca="teste", tipoDeLampada="LED", temperaturaDaLampada="branca", cor="azul", preco=10.00,
                       voltagem=220, ligada=False)

print(lampadaTeste.tipoDeLampada)
print(lampadaTeste.voltagem)
print(lampadaTeste.acende())
print(lampadaTeste.mostrar_preco())
