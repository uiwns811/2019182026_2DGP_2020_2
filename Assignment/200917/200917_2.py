from pico2d import *


angle = 30
length = 0.1
dx = 0.1 * cos(30 * 3.141592 / 180)
dy = 0.1 * sin(30 * 3.141592 / 180)
# dx = 0.1
# dy = 0.05

x = 100
y = 200

while True:	
	x += dx
	y += dy


open_canvas()

def handle_events() :
	global running, x, y, dx
	events = get_events();
	for e in events:
		if e.type == SDL_QUIT:
			running = False
		elif e.type == SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				running = False;
			elif e.key == SDLK_LEFT :
				dx -= 1
			elif e.key == SDLK_RIGHT:
				dx += 1
		elif e.type == SDL_KEYUP:
			if e.key == SDLK_ESCAPE:
				running = False;
			elif e.key == SDLK_LEFT :
				dx += 1
			elif e.key == SDLK_RIGHT:
				dx -= 1
		elif e.type == SDL_MOUSEMOTION:
			x, y = e.x, get_canvas_height() - e.y - 1


gra = load_image('resource/grass.png')
cha = load_image('resource/character.png')

x, y = get_canvas_width() // 2, get_canvas_height() // 2
dx = 0
running = True
hide_cursor()
while running:
# 이것을 게임물프라고 함. 무한반복
	clear_canvas()
	gra.draw(400, 30)
	cha.draw(x, y)
	update_canvas()
#로직 draw

	handle_events()

#랜더링 update
	x += dx * 4

	if x >= get_canvas_width() :
		break;

	delay(0.01)

close_canvas()