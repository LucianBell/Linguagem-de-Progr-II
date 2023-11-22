import pyxel
from classes.Level import Level

# Constantes das cores usadas
COLOR_D_BLUE = 1
COLOR_WHITE = 7
COLOR_RED = 8
COLOR_ORANGE = 9
COLOR_GREEN = 11


# Funções para desenhar as telas de:

# Fim de jogo
# (Com parâmetro com o score do jogador para ser mostrado na tela)
def draw_gameover_screen(score):
    pyxel.rect(0, 0, 128, 128, COLOR_D_BLUE)
    pyxel.text(56, 32, "GAME", COLOR_RED)
    pyxel.text(56, 42, "OVER ", COLOR_RED)
    pyxel.text(46, 52, "SCORE: " + str(score), COLOR_GREEN)
    pyxel.text(32, 72, "CLICK ESC TO QUIT", COLOR_ORANGE)
    pyxel.text(30, 82, "CLICK R TO RESTART", COLOR_GREEN)


# Começo do jogo (tela de início)
def draw_start_screen():
    pyxel.rect(0, 0, 128, 128, COLOR_D_BLUE)
    pyxel.text(42, 22, "Lil Wrench: ", COLOR_GREEN)
    pyxel.text(20, 32, "Colonization Adventure! ", COLOR_GREEN)
    pyxel.text(5, 52, "Arm yourself and take on alien", COLOR_WHITE)
    pyxel.text(5, 62, "adversaries and explore it all", COLOR_WHITE)
    pyxel.text(7, 72, "for humanity's expansion on", COLOR_WHITE)
    pyxel.text(32, 82, "this new planet.", COLOR_WHITE)
    pyxel.text(31, 102, "Click E to start.", COLOR_GREEN)


# Tela do nível do jogo
def draw_play_screen():
    Level().draw()
