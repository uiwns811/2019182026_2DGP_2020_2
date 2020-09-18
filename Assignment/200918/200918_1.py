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

gra = load_image(RES_DIR + '/grass.png')
cha = load_image(RES_DIR + '/run_animation.png')

x, y = 0, 85
fidx = 0
x2, y2 = 0, 200
running = True
while running:
	clear_canvas()
	gra.draw(400, 30)
	cha.clip_draw(fidx * 100, 0, 100, 100, x, y)
	cha.clip_draw(fidx * 100, 0, 100, 100, x2, y2)
	update_canvas()

	evts = get_events()

	handle_events()

	x += 2
	y += 1
	if x > get_canvas_width():
		running = False

	x2 += 1
	y2 += 0.5

	fidx = (fidx + 1) % 8

	delay(0.01)

close_canvas()