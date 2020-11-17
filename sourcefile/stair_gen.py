import random
import gfw
from pico2d import *
from stair import Stair

SPEED_PPS = 3000
GEN_X = [ 50, 150, 250, 350, 450 ]
next_wave = 0
wave_index = 0
stair_level = 0

def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()

def generate_wave():
    global wave_index, next_wave, stair_level
    x = random.choice(GEN_X)

    speed = -(100 + 5 * gfw.delta_time)
    e = Stair(x, speed)
    gfw.world.add(gfw.layer.stair, e)
    
    stair_level += 1
    next_wave = random.uniform(5, 6)

# LEVEL_ADJUST_PERCENTS = [ 10, 15, 15, 40, 15, 5 ] # -3 ~ 2
# # def stair_level():
#     percent = random.randrange(100)
#     pl = level
#     pp = percent
#     for p in LEVEL_ADJUST_PERCENTS:
#         if percent < p: break
#         percent -= p
#         level += 1
#     # print(pl, '->', level, ', ', pp, '->', percent)
#     if level < 1: level = 1
#     if level > 20: level = 20
#     return level

