"""
Crie uma classe chamada Relogio para armazenar um horário, composto por hora, minuto e segundo.
A classe deve representar esses componentes de horário e deve apresentar os métodos descritos a seguir:

um método chamado setHora, que deve receber o horário desejado por parâmetro (hora, minuto e segundo);
um método chamado getHora para retornar o horário atual, através de 3 variáveis passadas por referência;
um método para avançar o horário para o próximo segundo (lembre-se de atualizar o minuto e a hora,
quando for o caso).
"""

class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def set_hora(self, hora_desejada, min_desejado, segundo_desejado):
        self.hora = hora_desejada
        self.minuto = min_desejado
        self.segundo = segundo_desejado

    def get_hora(self):
        print(f"Hora: {self.hora}")
        print(f"Minuto: {self.minuto}")
        print(f"Segundo: {self.segundo}")

    def avancar_um_segundo(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
            if self.minuto == 60:
                self.minuto = 0
                self.hora += 1
                if self.hora == 24:
                    self.hora = 0


if __name__ == '__main__':
    relogio = Relogio(12, 30, 45)

    print("Horário atual:")
    relogio.get_hora()

    relogio.avancar_um_segundo()

    print("\nHorário após avançar um segundo:")
    relogio.get_hora()