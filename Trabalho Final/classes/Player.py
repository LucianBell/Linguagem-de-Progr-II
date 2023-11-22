import pyxel
from classes.CustomExceptions import OutOfBounds


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.direction = 1
        self.current_sprite = 0
        self.v_y = 0
        self.is_alive = True

    def update(self):
        try:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 1
                self.direction = 1
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 1
                self.direction = -1

            # Se o jogador ir para fora das bordas do nível...
            if self.x < 0 or self.x > 128:
                # Ele é recolocado na posição 10 no eixo x
                self.x = 10
                # É lançada a exceção
                raise OutOfBounds()

        except OutOfBounds as e:
            print(f"ERROR: {e}")

        if pyxel.btn(pyxel.KEY_SPACE):  # Pulo do jogador no espaço
            if self.y > 67:
                # Soma o movimento para cima aonde adiona a variável vy
                self.y += self.v_y
                self.v_y = min(self.v_y - 1, 1)

        # Ápice do pulo no qual começa a descida
        if self.y != 96 and self.y < 96:
            self.y += self.v_y
            self.v_y = min(self.v_y + 1, 1)

    def draw(self):
        # Param. u, criado com a formula para realizar a transição suave entre os dois sprites do personagem
        u = (pyxel.frame_count // 8 % 2) * 8

        # Se a direção for 1 (direita) é selecionado o sprite que aponta para a direita
        if self.direction == 1:
            pyxel.blt(self.x, self.y, 0, u, 0, self.w, self.h)
        else:
            # Caso o contrário, é selecionado o sprite que aponta para a esquerda
            pyxel.blt(self.x, self.y, 0, u, 8, self.w, self.h)
