import pyxel
from classes.CustomExceptions import OutOfBounds

COLOR_ORANGE = 10
bullets = []

"""
def shoot():
    bullets.append()
"""


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
                self.x += 0.8
                self.direction = 1
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 0.8
                self.direction = -1

            if self.x < 0 or self.x > 128:
                raise OutOfBounds()

        except OutOfBounds as e:
            print(f"ERROR: {e}")

        if pyxel.btn(pyxel.KEY_SPACE):  # Pulo do jogador no espaço
            if self.y > 67:
                # Soma ou movimento para cima aonde adiona a variável vy
                self.y += self.v_y
                self.v_y = min(self.v_y - 1, 1)
                pyxel.play(0, 4)

            # Ápice do pulo no qual começa a descida
        if self.y != 96 and self.y < 96:
            self.y += self.v_y
            self.v_y = min(self.v_y + 1, 1)
            pyxel.stop(0)

    def draw(self):
        u = (pyxel.frame_count // 8 % 2) * 8

        if self.direction == 1:
            pyxel.blt(self.x, self.y, 0, u, 0, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, u, 8, self.w, self.h)
