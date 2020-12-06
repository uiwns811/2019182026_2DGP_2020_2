from pico2d import *
import gfw

def init():
    global bg
    bg = gfw.image.load('res/image/background.png')
   
def draw():
    bg.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0)

def update():
	pass