import pyxel
import time


class WhiteFloor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 8, self.w, self.h)


# Main character
class RogerWaters:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.direction = "idle"
        self.spriteCount = 0
        self.jumpCount = 10
        self.isFalling = False
        self.isJumping = False

    def walking_right(self):
        if self.spriteCount == 1:
            pyxel.blt(self.x, self.y, 0, 16, 0, self.w, self.h)
            self.spriteCount = 2
        else:
            pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h)
            self.spriteCount = 1

    def walking_left(self):
        if self.spriteCount == 3:
            pyxel.blt(self.x, self.y, 0, 16, 8, self.w, self.h)
            self.spriteCount = 4
        else:
            pyxel.blt(self.x, self.y, 0, 8, 8, self.w, self.h)
            self.spriteCount = 3

    def jump(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, self.w, self.h)

    def draw(self):
        if self.direction == "idle":
            pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.walking_right()
            time.sleep(0.2)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.walking_left()
            time.sleep(0.2)
        elif pyxel.btn(pyxel.KEY_UP):
            self.jump()
            time.sleep(1)

    def set_direction(self, direction):
        self.direction = direction


class App:
    def __init__(self):
        pyxel.init(128, 128, title="Pink Floyd: No More Bricks!", display_scale=8, capture_scale=8, fps=60,
                   quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("../assets/my_resource.pyxres")
        self.rogerwaters = RogerWaters(64, 32)
        self.floor = WhiteFloor(0, 110)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.rogerwaters.set_direction("right")
            self.rogerwaters.x += 0.5
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.rogerwaters.set_direction("left")
            self.rogerwaters.x -= 0.5
        elif pyxel.btn(pyxel.KEY_UP):
            self.rogerwaters.y -= 0.5

        else:
            self.rogerwaters.set_direction("up")
            self.rogerwaters.set_direction("idle")

    def draw(self):
        pyxel.cls(0)
        self.rogerwaters.draw()
        self.floor.draw()


App()
