import pyxel

COLOR_BLACK = 0
COLOR_D_BLUE = 1
COLOR_PURPLE = 2
COLOR_CYAN = 3
COLOR_BROWN = 4
COLOR_L_BLUE = 5
COLOR_LL_BLUE = 6
COLOR_WHITE = 7
COLOR_RED = 8
COLOR_ORANGE = 9
COLOR_YELLOW = 10
COLOR_GREEN = 11
COLOR_KINDA_BLUE = 12
COLOR_GRAY = 13
COLOR_L_PINK = 14
COLOR_BEIGE = 15


def draw_gameover_screen():
    pyxel.rect(0, 0, 128, 128, COLOR_D_BLUE)
    pyxel.text(42, 22, "GAME", COLOR_RED)
    pyxel.text(20, 32, "OVER ", COLOR_RED)
