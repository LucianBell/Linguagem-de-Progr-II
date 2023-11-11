import pyxel
from classes.Enemy import Enemy
from classes.CustomExceptions import EnemyLoopError
from random import random, randint


class FooFighterEnemy(Enemy):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.speed = 1.5
        self.offset = int(random() * 60)

    def update_enemy(self):
        # Movimentação do Inimigo
        if (pyxel.frame_count + self.offset) % 30 < 30:
            self.x -= self.speed
        while self.x < 0:
            self.x = 120
            try:
                self.y = randint(60, 70)

                if self.y < 60 or self.y > 70:
                    raise EnemyLoopError()

            except EnemyLoopError as e:
                print(f"ERROR: {e}")

    def draw_enemy(self):
        u = (pyxel.frame_count // 14 % 2) * 8
        pyxel.blt(self.x, self.y, 0, u, 40, self.w, self.h)
