import random
from pico2d import *
import gfw
import gobj
from background import *

class Player:
    image = None

    #constructor
    def __init__(self):
        self.pos = get_canvas_width() // 2, 200
        self.delta = 0, 0
        self.speed = 200
        # 게임 시작 전 character_standard와 character_clock이 번갈아 나타나도록 구현
        self.image = gfw.image.load(gobj.res('/character_std.png'))
        # self.target_image = gfw.image.load(gobj.res('/character_clock.png'))
        self.time = 0
        self.fidx = 0
        self.action = 2
        self.mag = 1.0
        self.roll = 0
        self.width = self.image.w
        self.height = self.image.h
        self.stair_image = gfw.image.load(gobj.res('/stairs.png'))

    def draw(self):
        # pos = self.bg.to_screen(self.pos)
        self.image.draw(*self.pos)
        
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * self.mag * gfw.delta_time
        y += dy * self.speed * self.mag * gfw.delta_time

        px,py = x,y
        #bg_l, bg_b, bg_r, bg_t = self.bg.get_boundary()
        #x = clamp(bg_l, x, bg_r)
        #y = clamp(bg_b, y, bg_t)

        done = False

        self.time += gfw.delta_time
        frame = self.time * 15
        self.fidx = int(frame) % 5

    def get_bb(self):
        x, y = self.pos
        return x - self.width//2, y - self.height//2, x + self.width//2, y + self.height//2

    def reset(self):
        self.pos = get_canvas_width() - 100, 200
        self.image = gfw.image.load(gobj.res('/character_std.png'))
        self.left = self.pos[0] - self.image.w // 2
        self.bottom = self.pos[1] - self.image.h // 2
        self.right = self.left + self.image.w
        self.top = self.bottom + self.image.h

    def move_left(self):
        x, y = self.pos
        mx = x - self.stair_image.w
        my = y + self.stair_image.h
        self.pos = mx, my
        self.left, self.bottom, self.right, self.top = Player.get_bb(self)

    def get_roll(self):
        return self.roll

    def move(self):
        x, y = self.pos
        y += self.stair_image.h
        self.pos = x, y

    def handle_event(self, e):
        pair = (e.type, e.key)
        #self.stair_image = gfw.image.load(gobj.res('/stairs.png'))
        if e.type == SDL_MOUSEBUTTONDOWN:
            if self.pos[1] < self.stair_image.h * 3 + 200:
                self.move()
            # if self.pos[1] < self.stair_image.h + 200:
            #     self.pos = 3 * self.stair_image.w, 200 + self.stair_image.h
            #     self.left, self.bottom, self.right, self.top = Player.get_bb(self)
            #     self.image = gfw.image.load(gobj.res('/character_left.png'))
            # elif self.pos[1] < self.stair_image.h * 2 + 200:
            #     self.pos = 2 * self.stair_image.w, 200 + self.stair_image.h * 2
            #     self.left, self.bottom, self.right, self.top = Player.get_bb(self)
            #     self.image = gfw.image.load(gobj.res('/character_left.png'))
            # elif self.pos[1] < self.stair_image.h * 3 + 200:
            #     self.pos = 1 * self.stair_image.w, 200 + self.stair_image.h * 3
            #     self.left, self.bottom, self.right, self.top = Player.get_bb(self)
            #     self.image = gfw.image.load(gobj.res('/character_left.png'))

            # elif self.pos[1] < self.stair_image.h * 4 + 200:
            #     self.pos = 2 * self.stair_image.w, 200 + self.stair_image.h * 4
            #     self.left, self.bottom, self.right, self.top = Player.get_bb(self)
            #     self.image = gfw.image.load(gobj.res('/character_right.png'))

            # self.image = gfw.image.load(gobj.res('/character_left.png'))
    	 	# self.image = gfw.image.load(gobj.res('/character_clock.png'))
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE:
                self.roll = (self.roll + 1) % 2

            if self.roll % 2 == 0:
                self.image = gfw.image.load(gobj.res('/character_right.png'))
            if self.roll % 2 == 1:
                self.image = gfw.image.load(gobj.res('/character_left.png'))
