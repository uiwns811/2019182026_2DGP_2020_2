from pico2d import *
import gfw
import gobj
import random

class Coins:
	FPS =100
	def __init__(self, pos, delta):
		self.pos = pos
		self.delta = delta
		self.image = gfw.image.load(gobj.res('/coins.png'))
		self.time = get_time()
		self.size = self.image.h
		self.radius = self.size // 2
		self.bb_l = -self.size
		self.bb_b = -self.size
		self.bb_r = get_canvas_width() + self.size
		self.bb_t = get_canvas_height() + self.size
		self.fcount = self.image.w // self.image.h
		# self.left = self.x - gfw.

	def update(self):
		pass

	def draw(self):
		elapsed = get_time() - self.time
		fidx = round(elapsed + Coins.FPS) % self.fcount
		size = self.image.h
		rect = fidx * size, 0, size, size
		self.image.clip_draw(*rect, *self.pos, self.size, self.size)

	def move(self, dx):
		self.x += dx
		if self.y - COIN_HEIGHT < 0:
			gfw.world.remove(self)

	# def get_bb(self):
	# 	return 
