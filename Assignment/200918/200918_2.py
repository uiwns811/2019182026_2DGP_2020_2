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
	def __init__(self, pos, delta):
		self.x, self.y = pos
		self.dx, self.dy = delta
		self.fidx = 0
		self.image = load_image(RES_DIR + '/run_animation.png')
	def draw(self) :
		self.image.clip_draw(self.fidx*100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx
		self.y += self.dy

grass = Grass()
boy = Boy((0, 85), (2, 0.1)) 
boy2 = Boy((0, 200), (1, 0.05)) 

running = True
while running:
	clear_canvas()
	grass.draw()
	boy.draw()
	boy2.draw()
	update_canvas()

	evts = get_events()

	handle_events()

	boy.update()
	boy2.update()
	grass.update()

	boy.x += 2
	boy.y += 1
	if boy.x > get_canvas_width():
		running = False
	if boy2.x > get_canvas_width():
		running = False


	boy2.x += 1
	boy2.y += 0.5

	boy.fidx = (boy.fidx + 1) % 8
	boy2.fidx = (boy2.fidx + 1) % 8

	delay(0.01)

close_canvas()