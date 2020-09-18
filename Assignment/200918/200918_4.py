from gobj import *
from pico2d import *

def handle_events():
	global running
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif (e.type, e.key) ==  (SDL_KEYDOWN, SDLK_ESCAPE):
			running = False

open_canvas()

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