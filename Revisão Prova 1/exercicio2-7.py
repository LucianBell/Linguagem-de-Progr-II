"""
Crie uma classe chamada Relogio para armazenar um horário, composto por hora, minuto e segundo. A classe deve representar esses componentes de horário e deve apresentar os métodos descritos a seguir:
um método chamado setHora, que deve receber o horário desejado por parâmetro (hora, minuto e segundo);
um método chamado getHora para retornar o horário atual, através de 3 variáveis passadas por referência;
um método para avançar o horário para o próximo segundo (lembre-se de atualizar o minuto e a hora, quando for o caso).
"""


class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def set_hora(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def get_hora(self):
        hora_atual = self.__hora
        minuto_atual = self.__minuto
        segundo_atual = self.__segundo

        print(f"Hora: {hora_atual}. Minuto: {minuto_atual}. Segundo: {segundo_atual}")

