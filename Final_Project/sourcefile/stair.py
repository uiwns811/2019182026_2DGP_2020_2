from pico2d import *
import gfw
from gobj import *

class Stair:
    SIZE = 30
    def __init__(self, x, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, get_canvas_height() + Stair.SIZE
        self.dx, self.dy = 0, speed
        self.image = gfw.image.load(RES_DIR + '/stair.png')
        self.fidx = 0
        self.src_width = self.image.w // 8
        self.src_height = self.image.h
        self.time = 0

    def draw(self):
        sx = self.fidx * self.src_width
        self.image.draw(self.x, self.y)
        gy = self.y - Stair.SIZE // 2 

    def update(self):
        self.time += gfw.delta_time
        self.fidx = int(self.time * 10 + 0.5) % 8
        # self.x += self.dx
        self.y += self.dy * gfw.delta_time

        if self.y < -Stair.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    # def decrease_life(self, amount):
    #     self.life -= amount
    #     return self.life <= 0

    # def score(self):
    #     return self.max_life

    def get_bb(self):
        half = Stair.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half
