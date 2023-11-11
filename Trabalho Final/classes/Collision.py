import pyxel
import random
from random import random
from random import randint
from classes.Player import Player
from classes.FooFighterEnemy import FooFighterEnemy
from classes.TerrestrialEnemy import TerrestrialEnemy
from classes.Screens import draw_gameover_screen

class Colision(Player, TerrestrialEnemy):
    def __init__(self):
        Player.__init__(self, 58, 96)
        TerrestrialEnemy.__init__(self, 120, 96)

    def ColisionUpdate(self):
        if ((self.x + 3 == self.x_Ene - 2) or (self.x + 3 == self.x_Ene - 2.25) or (
                self.x + 3 == self.x_Ene - 2.50) or (self.x + 3 == self.x_Ene - 2.75) or (
                self.x + 3 == self.x_Ene - 3.0)):
            if self.playerAlive:
                # jogador morre
                self.playerAlive = False
                # reset score e posição
                self.score = 0
                self.x = 20
                self.y = 90
                self.player_vy = 0
                self.playerAlive = True
                self.x_Ene = 200
                self.y_Ene = 90
                self.w_Ene = 16
                self.h_Ene = 16
                self.EneSpeed = 1


class MyColisionSystem:
    def __init__(self, Player, Enemy):
        Player.__init__()
        Enemy.__init__()

    def check_collision(self):
        if  == self.enemy_x and self.player_y == self.enemy_y:
            draw_gameover_screen()
            pyxel.stop(0)
