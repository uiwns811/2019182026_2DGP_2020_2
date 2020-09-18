from pico2d import *

open_canvas()

gra = load_image('resource/grass.png')
cha = load_image('resource/character.png')

x = 0 
while (x < 800) :
	clear_canvas()
	gra.draw(400, 30)
	cha.draw(x, 90)
	x += 5
	update_canvas()
	delay(0.01)
	get_events()


delay(2)

close_canvas()
