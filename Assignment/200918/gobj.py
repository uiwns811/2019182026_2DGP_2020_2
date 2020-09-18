from pico2d import *
import random
RES_DIR = 'resource'

class Grass:
	def __init__(self):
		self.image = load_image(RES_DIR + '/grass.png')
	def draw(self):
		self.image.draw(400, 30)
	def update(self):
		pass

class Boy:
	def __init(self):
		self.x , self.y = random.randint(100, 700), random.randint(100, 500)
		self.dx, self.dy = random.randint(), random.randint()
		self.fidx = random.randint(0, 7)
		self.image = load_image(RES_DIR + '/run_animation.png')
	def draw(self):
		self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.fidx = (self.fidx + 1) % 8
