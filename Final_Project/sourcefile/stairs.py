import gfw
import random
from gobj import *

SPEED_PPS = 3000
MAG_SPEED = 0.15
stair_level = 0
stair_width = 118
stair_height = 65

prev_index = 5
cur_index = 0


class Stair(AnimObject):
    def __init__(self, value):
        fn = 'stairs.png'
        # super(Stair, self).__init__(fn, (0, 0), 10)
        self.image = gfw.image.load(res(fn))
        self.being_born = True
        self.mag = 0
        self.stair_level = 0

    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.fps) % self.fcount
        sx = self.width * fidx
        size = self.width * self.mag, self.height * self.mag
        self.image.clip_draw(sx, 0, self.width, self.height, *self.pos, *size)
    
    # def update(self):
    
    def generate_stair():
        global stair_level, prev_index, cur_index
        stair_level += 1
        # i = random.randint(0, 15)
        # x = i % 4
        # x구현하기 
        if prev_index > 0:
            cur_index = prev_index - 1
            prev_index -= 1
        if prev_index <= 0:
            cur_index = prev_index + 1
            prev_index += 1
        x = (cur_index) * stair_width + 110
        if stair_level < 12:
            y = (12 - stair_level) * stair_height + 110
        else:
            y = 0 + 110
        # y = get_canvas_height() - 30 - 30 * stair_level
        return (x, y)    

    def remove(self):
        gfw.world.remove(self)

    def __del__(self):
        print("Removing", self)