from pico2d import *
import gfw
import gobj
import random

COIN_WIDDTH = 85
COIN_HEIGHT = 80

def get_coin_rect(index):
	ix, iy = index % 30, index // 30

class Coins:
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.image = gfw.image.load(gobj.res('/coins.png'))
		index = random.randint(3, 60)
		self.rect = get_coin_rect(index)
		self.mag = 1
		# self.left = self.x - gfw.

	def update(self):
		pass

	def draw(self):
		self.image.clip_draw(0, 0, 80, 80, self.x, self.y)

	def move(self, dx):
		self.x += dx
		if self.y - COIN_HEIGHT < 0:
			gfw.world.remove(self)

	# def get_bb(self):
	# 	return 
