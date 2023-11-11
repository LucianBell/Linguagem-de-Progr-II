import time

import pyxel
import sys
from random import randint

from classes.Player import Player
from classes.Level import Level
from classes.TerrestrialEnemy import TerrestrialEnemy
from classes.FooFighterEnemy import FooFighterEnemy
from classes.Collision import MyColisionSystem

sys.path.insert(0, "..")
bullets = []

START = 0
PLAY = 1

COLOR_BLUE = 1
COLOR_GREEN = 3
COLOR_WHITE = 7
COLOR_RED = 8
COLOR_L_GREEN = 11
COLOR_PINK = 14


def draw_start_screen():
    pyxel.rect(0, 0, 128, 128, COLOR_BLUE)
    pyxel.text(42, 22, "Lil Wrench: ", COLOR_GREEN)
    pyxel.text(20, 32, "Colonization Adventure! ", COLOR_L_GREEN)
    pyxel.text(5, 52, "Arm yourself and take on alien", COLOR_WHITE)
    pyxel.text(5, 62, "adversaries, clearing the way", COLOR_WHITE)
    pyxel.text(5, 72, "for humanity's expansion on", COLOR_WHITE)
    pyxel.text(32, 82, "this new planet.", COLOR_WHITE)
    pyxel.text(31, 102, "Click E to start.", COLOR_GREEN)


def draw_play_screen():
    Level().draw()


class App:
    def __init__(self):
        # Função para inicializar o jogo com as especs mais relevantes sendo:
        # Largura da tela e altura da tela: 128pxs, e tecla para sair do jogo: ESC.
        pyxel.init(128, 128, title="Lil Wrench: Colonization Adventure!", display_scale=8, capture_scale=8, fps=60,
                   quit_key=pyxel.KEY_ESCAPE)

        # Função para carregar o arquivo com os recursos do jogo (músicas, efeitos sonoros, sprites...)
        pyxel.load("../assets/my_resource.pyxres")

        # Tocar a música 0 em loop
        pyxel.playm(0, loop=True)

        # Atributos do jogo: Tela atua, robô (instância de Player), inimigo (instância de TerrestrialEnemy)
        # inimigo voador (instância de FooFighterEnemy) e pontuação (recebe uma int que é incrementada por segundo)
        self.screen = START
        self.robot = Player(58, 96)
        self.enemy = TerrestrialEnemy(120, 96)
        self.flying_enemy = FooFighterEnemy(120, 70)
        self.collision_terrestrial = MyColisionSystem(player_x=self.robot.x, player_y=self.robot.y,
                                                      enemy_x=self.enemy.x, enemy_y=self.enemy.y)
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        # Se o atributo scren receber start...
        if self.screen == START:
            # Chama a função que desenha a tela inicial com texto e ...
            draw_start_screen()
            # Se a tecla E for pressionada, screen recebe 'PLAY' e o jogo é iniciado
            if pyxel.btnp(pyxel.KEY_E):
                self.screen = PLAY
        # Se a tela estiver com string 'PLAY'
        if self.screen == PLAY:
            # Chama os métodos update de cada atributo instanciado (robot, enemy, flying_enemy)
            self.robot.update()
            self.enemy.update_enemy()
            self.flying_enemy.update_enemy()
            self.collision_terrestrial.check_collision()

            # Se o robo estiver vivo, score recebe +1 a cada segundo
            if self.robot.is_alive:
                self.score += 1

    def draw(self):
        # Se estiver na tela 'PLAY'
        if self.screen == PLAY:
            # Chama a função que 
            draw_play_screen()
            self.robot.draw()
            self.enemy.draw_enemy()
            self.flying_enemy.draw_enemy()
            pyxel.text(5, 12, "SCORE: " + str(self.score), 7)


App()
