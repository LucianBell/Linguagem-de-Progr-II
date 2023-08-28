"""
Implemente um carro. O tanque de combustível do carro armazena no máximo 50 litros de gasolina.
O carro consome 15 km/litro. Deve ser possível:
Abastecer o carro com uma certa quantidade de gasolina.
Mover o carro em uma determinada distância (medida em km);
Retornar a quantidade de combustível e a distância total percorrida.
No programa principal, crie 2 carros. Abasteça 20 litros no primeiro e 30 litros no segundo.
Desloque o primeiro em 200 km e o segundo em 400 km. Exiba na tela a distância percorrida e o total de
combustível restante para cada um.
"""


class Carro:
    def __init__(self, gasolina, distancia_percorrida):
        if gasolina > 50:
            self.gasolina = 50
            print(f"Tanque só suporta 50L. Tanque abastecido com 50L")
        else:
            self.gasolina = gasolina
            self.distancia_percorrida = distancia_percorrida

    def abastecer(self, quantidade_inserida):
        if self.gasolina + quantidade_inserida > 50:
            print(f"Tanque só suporta 50L. Tanque abastecido com 50L")
            self.gasolina = 50
        else:
            self.gasolina += quantidade_inserida

    def viajar(self, quantidade_kilometros):
        consumo = quantidade_kilometros / 15
        if consumo <= self.gasolina:
            self.gasolina -= consumo
            self.distancia_percorrida += quantidade_kilometros

    def mostrar_dados(self):
        print("DADOS:")
        print(f"Gasolina: {self.gasolina: .2f}")
        print(f"Distância percorrida: {self.distancia_percorrida}")


if __name__ == '__main__':
    carro1 = Carro(20, 0)
    carro2 = Carro(30, 0)

    carro1.viajar(200)
    carro2.viajar(400)

    print("Carro 1:")
    carro1.mostrar_dados()

    print("\nCarro 2:")
    carro2.mostrar_dados()