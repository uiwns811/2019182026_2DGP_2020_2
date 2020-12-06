import gfw
from pico2d import *
import gobj
import game_state

TEXT_COLOR = (255, 212, 0)

def enter():
	global logo_image, bg_image, font
	bg_image = gfw.image.load(gobj.res('/blue.png'))
	logo_image = gfw.image.load(gobj.res('/logo_infinite_stairs.png'))
	font = gfw.font.load('res/font/FlappyFont.TTF', 40)

def update():
	pass

def draw():
	bg_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
	logo_image.draw(350, 700)
	font.draw(190, 450, 'START -> "ENTER"', TEXT_COLOR)
	font.draw(150, 300, 'STEP UP -> "MOUSE"', (0, 0, 0))
	font.draw(150, 250, 'TURN     -> "SPACE"', (0, 0, 0))
	font.draw(150, 50, '2019182026 LEESUMIN', (255, 255, 255))
	

def handle_event(e):
	if e.type == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_KEYDOWN:
		if e.key == SDLK_ESCAPE:
			gfw.quit()
		elif e.key == SDLK_RETURN:
			gfw.change(game_state)

def exit():
	global logo_image, bg_image
	gfw.image.unload(gobj.res('/blue.png'))
	gfw.image.unload(gobj.res('/logo_infinite_stairs.png'))
	del logo_image
	del bg_image

def pause():
	pass

def resume():
	pass

if __name__ == '__main__':
    gfw.run_main()