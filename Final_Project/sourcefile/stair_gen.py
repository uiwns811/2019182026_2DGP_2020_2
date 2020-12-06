from pico2d import *
import gfw
from stair import *
import random

STAIR_COUNT = 13
ITEM_COUNT = 2

SPEED_PPS = 3000
MAG_SPEED = 0.15
stair_level = 0
# STAIR_WIDTH = 118 132
# STAIR_HEIGHT = 65 72

prev_index = 2  # 이전 계단의 인덱스
cur_index = 0   # 현재 계단의 인덱스
cnt_dec = 0     # 왼쪽으로의  증가폭
cnt_inc = 0     # 오른쪽으로의 증가폭 

# 매 프레임마다 불리는 함수, 최초에 한 번만 불리는 함수
def init():
    pass

def get_xy(prev):
    global stair_level
    newX = 0
    newY = 0
    prevX, prevY = prev
    image_w = 148
    image_h = 88
    xdirection = random.randint(0, 1)
    if xdirection == 0:
        newX = prevX - image_w
    else:
        newX = prevX + image_w

    newY = prevY + image_h

    return newX, newY

def update():
    while gfw.world.count_at(gfw.layer.stairs) < STAIR_COUNT:
        generate()
    while gfw.world.count_at(gfw.layer.item) < ITEM_COUNT:
        generate_item()
        
def generate():
    x, y, stair_ylevel, xdirection = get_coords()
    s = Stair((x,y), stair_ylevel, xdirection)     # pos, delta가 인자이므로 튜플로 묶어서 전달
    s.draw()
    gfw.world.add(gfw.layer.stairs, s)

def sub_generate(pos):
    xdirection = 1
    print(xdirection)
    s = Stair(pos, 13, xdirection)
    gfw.world.add(gfw.layer.stairs, s)

def generate_item():
    x, y, item_ylevel, xdirection = get_coords()
    c = Coin((x,y), item_ylevel)
    gfw.world.add(gfw.layer.item, c)

def get_coords():           # 좌표를 생성하는 함수를 만들자.. missile말고 item도 만들건데 생성되는 x, y, dx, dy를 결정하는게 따로 필요.
    global stair_level, prev_index, cur_index
    image = gfw.image.load('res/image/stairs.png')
    xdirection = random.randint(0, 1)      # 계단의 생성 방향 결정

    if stair_level == 3:
        cur_index = 3
    
    if xdirection == 0:
        if prev_index < 1:      # 더이상 왼쪽으로 갈 수 없는 경우
            cur_index = prev_index + 1
            prev_index = cur_index
            # xdirection = 1
        else:
            cur_index = prev_index - 1
            prev_index = cur_index

    if xdirection == 1:
        if prev_index > 3:      # 더이상 오른쪽으로 갈 수 없는 경우
            cur_index = prev_index - 1
            prev_index = cur_index 
            # xdirection = 0
        else:
            cur_index = prev_index + 1
            prev_index = cur_index

    x = (cur_index) * image.w + 50    # x의 화면상의 위치 표시
    y = stair_level * image.h + 120  # y의 화면상의 위치 표시
    stair_level += 1        #계단의 높이 (최대 12)
    
    return x, y, stair_level, xdirection