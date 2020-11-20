from pico2d import *
import gfw

def init(p):
    global bg, player
    bg = gfw.image.load('../res/image/background.png')
    player = p      # player의 위치에 따라 매번 다르게 그림

def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2        # 화면의 중심
    px, py = player.pos         #player의 위치
    dx, dy = px - x, py - y     #화면 중심에서 player가 얼마나 떨어져있는지 (x 기준 0~400 가능)
    bg.draw(x - dx * 0.05, y - dy * 0.05)

def update():
    pass