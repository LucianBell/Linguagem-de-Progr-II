import pyxel

from classes.Player import Player
from classes.TerrestrialEnemy import TerrestrialEnemy
from classes.FooFighterEnemy import FooFighterEnemy
from classes.CustomExceptions import ScreenDrawingError
from classes.Screens import draw_gameover_screen, draw_start_screen, draw_play_screen

# Constantes usadas para determinar o estado do jogo
START = 0
PLAY = 1
GAME_OVER = 2


class App:
    def __init__(self):
        pyxel.init(128, 128, title="Lil Wrench: Colonization Adventure!", display_scale=8, capture_scale=8, fps=60,
                   quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("../assets/my_resource.pyxres")

        pyxel.playm(1, loop=True)

        # Atributos do jogo: Tela atua, robô (instância de Player), inimigo (instância de TerrestrialEnemy)
        # inimigo voador (instância de FooFighterEnemy) e pontuação
        self.screen = START
        self.robot = Player(58, 96)
        self.enemy = TerrestrialEnemy(120, 96)
        self.flying_enemy = FooFighterEnemy(120, 70)
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

            # Sistema de colisão chamado pela função "collision_system":
            self.collision_system()

            # Se o robo estiver vivo, score recebe +1 a cada segundo
            if self.robot.is_alive:
                self.score += 1

        if self.screen == GAME_OVER:
            if pyxel.btn(pyxel.KEY_R):
                self.screen = START
                self.score = 0
                self.robot = Player(58, 96)
                self.enemy = TerrestrialEnemy(120, 96)
                self.flying_enemy = FooFighterEnemy(120, 70)
                pyxel.run(self.update, self.draw)

    def draw(self):
        try:
            if self.screen == PLAY:
                # Chama funções que mostram na tela o cenário, o personagem principal, o inimigo terrestre,
                # o inimigo voador e o score do jogador
                draw_play_screen()
                self.robot.draw()
                self.enemy.draw_enemy()
                self.flying_enemy.draw_enemy()
                pyxel.text(5, 12, "SCORE: " + str(self.score), 7)
            if self.screen == GAME_OVER:
                # Chama a função para mostrar a tela de fim de jogo
                draw_gameover_screen(self.score)

            if self.screen != PLAY and self.screen != GAME_OVER and self.screen != START:
                raise ScreenDrawingError()

        except ScreenDrawingError as e:
            print(f"ERROR: {e}")

    # Função que faz a checagem da posição do jogador e dos inimigos, funcionando como sistema de colisão
    def collision_system(self):
        if ((self.robot.x + 3 == self.enemy.x - 2) or (self.robot.x + 3 == self.enemy.x - 2.25) or (
                self.robot.x + 3 == self.enemy.x - 2.50) or (self.robot.x + 3 == self.enemy.x - 2.75) or (
                    self.robot.x + 3 == self.enemy.x - 3.0)) and self.robot.y == self.enemy.y:
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x + 1 == self.enemy.x + 2) or (self.robot.x + 1 == self.enemy.x + 2.25) or (
                self.robot.x + 1 == self.enemy.x + 2.50) or (self.robot.x + 1 == self.enemy.x + 2.75) or (
                    self.robot.x + 1 == self.enemy.x + 3.0)) and self.robot.y == self.enemy.y:
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x - 3 == self.enemy.x + 2) or (self.robot.x - 3 == self.enemy.x + 2.25) or (
                self.robot.x - 3 == self.enemy.x + 2.50) or (self.robot.x - 3 == self.enemy.x + 2.75) or (
                    self.robot.x - 3 == self.enemy.x + 3.0)) and self.robot.y == self.enemy.y:
            self.robot.is_alive = False
            self.screen = GAME_OVER
        # Sistema de colisão para o inimigo voador
        if ((self.robot.x + 3 == self.flying_enemy.x - 2) or (self.robot.x == self.flying_enemy.y) or (
                self.robot.x + 3 == self.flying_enemy.x - 2.25) or (
                    self.robot.x + 3 == self.flying_enemy.x - 2.50) or (
                    self.robot.x + 3 == self.flying_enemy.x - 2.75) or (
                    self.robot.x + 3 == self.flying_enemy.x - 3.0)) and (
                (self.robot.y == self.flying_enemy.y) or (self.robot.y == self.flying_enemy.y - 1) or (
                self.robot.y == self.flying_enemy.y - 1.25) or (self.robot.y == self.flying_enemy.y - 1.5) or (
                        self.robot.y == self.flying_enemy.y - 1.75) or (
                        self.robot.y == self.flying_enemy.y - 2.0)):
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x + 1 == self.flying_enemy.x + 2) or (
                self.robot.x + 1 == self.flying_enemy.x + 2.25) or (
                    self.robot.x + 1 == self.flying_enemy.x + 2.50) or (
                    self.robot.x + 1 == self.flying_enemy.x + 2.75) or (
                    self.robot.x + 1 == self.flying_enemy.x + 3.0)) and (
                (self.robot.y == self.flying_enemy.y + 2) or (self.robot.y == self.flying_enemy.y - 2) or (
                self.robot.y == self.flying_enemy.y - 2.25) or (self.robot.y == self.flying_enemy.y - 2.5) or (
                        self.robot.y == self.flying_enemy.y - 2.75)):
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x - 3 == self.flying_enemy.x + 2) or (
                self.robot.x - 3 == self.flying_enemy.x + 2.25) or (
                    self.robot.x - 3 == self.flying_enemy.x + 2.50) or (
                    self.robot.x - 3 == self.flying_enemy.x + 2.75) or (
                    self.robot.x - 3 == self.flying_enemy.x + 3.0)) and (
                (self.robot.y == self.flying_enemy.y + 3) or (self.robot.y == self.flying_enemy.y - 3) or (
                self.robot.y == self.flying_enemy.y - 3.25) or (self.robot.y == self.flying_enemy.y - 3.5) or (
                        self.robot.y == self.flying_enemy.y - 3.75) or (
                        self.robot.y == self.flying_enemy.y - 4.0)):
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x - 3 == self.flying_enemy.x + 2) or (
                self.robot.x - 3 == self.flying_enemy.x + 2.25) or (
                    self.robot.x - 3 == self.flying_enemy.x + 2.50) or (
                    self.robot.x - 3 == self.flying_enemy.x + 2.75) or (
                    self.robot.x - 3 == self.flying_enemy.x + 3.0)) and (
                (self.robot.y == self.flying_enemy.y + 4) or (self.robot.y == self.flying_enemy.y - 4) or (
                self.robot.y == self.flying_enemy.y - 4.25) or (
                        self.robot.y == self.flying_enemy.y - 4.5) or (
                        self.robot.y == self.flying_enemy.y - 4.75) or (
                        self.robot.y == self.flying_enemy.y - 5.0)):
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x + 3 == self.flying_enemy.x - 2) or (self.robot.x == self.flying_enemy.y) or (
                self.robot.x + 3 == self.flying_enemy.x - 2.25) or (
                    self.robot.x + 3 == self.flying_enemy.x - 2.50) or (
                    self.robot.x + 3 == self.flying_enemy.x - 2.75) or (
                    self.robot.x + 3 == self.flying_enemy.x - 3.0)) and (
                (self.robot.y == self.flying_enemy.y) or (self.robot.y == self.flying_enemy.y + 1) or (
                self.robot.y == self.flying_enemy.y + 1.25) or (
                        self.robot.y == self.flying_enemy.y + 1.5) or (
                        self.robot.y == self.flying_enemy.y + 1.75) or (
                        self.robot.y == self.flying_enemy.y + 2.0)):
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x + 1 == self.flying_enemy.x + 2) or (
                self.robot.x + 1 == self.flying_enemy.x + 2.25) or (
                    self.robot.x + 1 == self.flying_enemy.x + 2.50) or (
                    self.robot.x + 1 == self.flying_enemy.x + 2.75) or (
                    self.robot.x + 1 == self.flying_enemy.x + 3.0)) and (
                (self.robot.y == self.flying_enemy.y + 2) or (self.robot.y == self.flying_enemy.y + 2) or (
                self.robot.y == self.flying_enemy.y + 2.25) or (
                        self.robot.y == self.flying_enemy.y + 2.5) or (
                        self.robot.y == self.flying_enemy.y + 2.75)):
            self.robot.is_alive = False
            self.screen = GAME_OVER
        if ((self.robot.x - 3 == self.flying_enemy.x + 2) or (
                self.robot.x - 3 == self.flying_enemy.x + 2.25) or (
                    self.robot.x - 3 == self.flying_enemy.x + 2.50) or (
                    self.robot.x - 3 == self.flying_enemy.x + 2.75) or (
                    self.robot.x - 3 == self.flying_enemy.x + 3.0)) and (
                (self.robot.y == self.flying_enemy.y + 3) or (self.robot.y == self.flying_enemy.y + 3) or (
                self.robot.y == self.flying_enemy.y + 3.25) or (
                        self.robot.y == self.flying_enemy.y + 3.5) or (
                        self.robot.y == self.flying_enemy.y + 3.75) or (
                        self.robot.y == self.flying_enemy.y + 4.0)):
            self.robot.is_alive = False
            self.screen = GAME_OVER


App()
