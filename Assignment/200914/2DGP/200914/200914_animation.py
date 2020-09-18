from pico2d import *

open_canvas()

gra = load_image('resource/grass.png')
cha = load_image('resource/animation_sheet.png')

frame = 0
x = 0
while (x < 800) :
	clear_canvas()
	gra.draw(400, 30)
	cha.clip_draw(frame*100, 100, 100, 100, x, 90)
	x += 10
	frame = (frame+1) %8
	update_canvas()
	get_events()
	delay(0.03)

close_canvas()
