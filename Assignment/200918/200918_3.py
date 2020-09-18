import random
from pico2d import *

RES_DIR = 'resource'

def handle_events():
	global running
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif (e.type, e.key) ==  (SDL_KEYDOWN, SDLK_ESCAPE):
			running = False

open_canvas()

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
		self.load_image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.fidx = (self.fidx + 7) % 8

grass = Grass()
team = [ Boy() for i in range(11) ]

running = True
while running:
	clear_canvas()
	grass.draw()
	for boy in team:
		boy.draw()
	update_canvas()

	evts = get_events()

	handle_events()

	for boy in team:
		boy.update

	delay(0.01)

close_canvas()