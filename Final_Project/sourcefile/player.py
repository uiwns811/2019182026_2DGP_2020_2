import random
from pico2d import *
import gfw
import gobj
from background import *

class Player:
    image = None

    #constructor
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.delta = 0, 0
        self.speed = 200
        # 게임 시작 전 character_standard와 character_clock이 번갈아 나타나도록 구현
        self.image = gfw.image.load(gobj.res('/character_standard.png'))
        # self.target_image = gfw.image.load(gobj.res('/character_clock.png'))
        self.time = 0
        self.fidx = 0
        self.action = 2
        self.mag = 1
        self.roll = 0

    def draw(self):
        pos = self.bg.to_screen(self.pos)
        self.image.draw(*self.pos)

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * self.mag * gfw.delta_time
        y += dy * self.speed * self.mag * gfw.delta_time

        px,py = x,y
        bg_l, bg_b, bg_r, bg_t = self.bg.get_boundary()
        x = clamp(bg_l, x, bg_r)
        y = clamp(bg_b, y, bg_t)

        done = False

        self.time += gfw.delta_time
        frame = self.time * 15
        self.fidx = int(frame) % 5

    def handle_event(self, e):
    	pair = (e.type, e.key)
    	if e.type == SDL_MOUSEBUTTONDOWN:
    	 	self.image = gfw.image.load(gobj.res('/character_clock.png'))

    	if e.type == SDL_KEYDOWN:
	    	if e.key == SDLK_SPACE:
    			self.roll += 1
    			
    			if self.roll % 2 == 0:
    				self.image = gfw.image.load(gobj.res('/character_right.png'))
    				
    			if self.roll % 2 == 1:
    				self.image = gfw.image.load(gobj.res('/character_left.png'))
