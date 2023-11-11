import pyxel


class Level:
    def __init__(self):
        self.tile_map = 0
        self.u = 0
        self.v = 0
        self.score = 0
        self.w = 128
        self.h = 120

    def draw(self):
        offset = pyxel.frame_count % 128
        for loop in range(2):
            pyxel.bltm(loop * 128 - offset, 0, self.tile_map, 0, 0, 128, 120, colkey=pyxel.COLOR_BLACK)

