from pico2d import *
from gfw import *
from stairs import *
import random
import gobj

def generate_stair():
	stair = Stair()
	gfw.world.add(gfw.layer.stairs, stair)
	print('creating stairs')

# def generate_stair():
# 	global STAIR_HEIGHT, cnt, stair_level
# 	x, y, stair_level = Stair.generate_stair()
# 	y -= STAIR_HEIGHT * stair_level
# 	fn = 'stairs.png'
# 	stair = gobj.AnimObject(fn, (x,y), 10)
# 	gfw.world.add(gfw.layer.stair, stair)