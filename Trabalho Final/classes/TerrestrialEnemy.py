import pyxel
from classes.Enemy import Enemy
from classes.CustomExceptions import EnemyLoopError
from random import random, randint


class TerrestrialEnemy(Enemy):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.speed = 0.5
        self.which_skin = randint(1, 3)
        self.offset = int(random() * 60)

    def update_enemy(self):
        # Movimentação do Inimigo
        if (pyxel.frame_count + self.offset) % 30 < 30:
            self.x -= self.speed

        if self.which_skin == 1:
            self.speed = 0.5
        elif self.which_skin == 2:
            self.speed = 1.5
        elif self.which_skin == 3:
            self.speed = 1.5

        while self.x < 0:
            try:
                self.x = 120
                self.y = 96
                self.which_skin = randint(1, 3)

                if self.x != 120 or self.y != 96:
                    raise EnemyLoopError()

            except EnemyLoopError as e:
                print(f"ERROR: {e}")

    def draw_enemy(self):
        u = (pyxel.frame_count // 14 % 2) * 8
        if self.which_skin == 1:
            pyxel.blt(self.x, self.y, 0, u, 16, self.w, self.h)
        elif self.which_skin == 2:
            pyxel.blt(self.x, self.y, 0, u, 24, self.w, self.h)
        elif self.which_skin == 3:
            pyxel.blt(self.x, self.y, 0, u, 32, self.w, self.h)
