from pico2d import *
import gfw
from stair import Stair
import random

STAIR_COUNT = 13

SPEED_PPS = 3000
MAG_SPEED = 0.15
stair_level = 0
STAIR_WIDTH = 118
STAIR_HEIGHT = 65

prev_index = random.randint(0, 4)  # 이전 계단의 인덱스
cur_index = 0   # 현재 계단의 인덱스
cnt_dec = 0     # 왼쪽으로의  증가폭
cnt_inc = 0     # 오른쪽으로의 증가폭 

# 매 프레임마다 불리는 함수, 최초에 한 번만 불리는 함수
def init():
    pass

def update():
    while gfw.world.count_at(gfw.layer.stairs) < STAIR_COUNT:
        generate()

def generate():
    x, y = get_coords()
    s = Stair((x,y))     # pos, delta가 인자이므로 튜플로 묶어서 전달
    gfw.world.add(gfw.layer.stairs, s)

def get_coords():           # 좌표를 생성하는 함수를 만들자.. missile말고 item도 만들건데 생성되는 x, y, dx, dy를 결정하는게 따로 필요.
    global stair_level, prev_index, cur_index
    randcnt = random.randint(0, 1)      # 계단의 증감폭 랜덤값으로 설정
        # i = random.randint(0, 15)
        # x = i % 4
        # x구현하기 
    if randcnt == 0:
        if prev_index < 1:      # 더이상 왼쪽으로 갈 수 없는 경우
            cur_index = prev_index + 1
            prev_index += 1
        else:
            cur_index = prev_index - 1
            prev_index -= 1

    if randcnt == 1:
        if prev_index > 3:      # 더이상 오른쪽으로 갈 수 없는 경우
            cur_index = prev_index - 1
            prev_index -= 1
        else:
            cur_index = prev_index + 1
            prev_index += 1

    x = (cur_index) * STAIR_WIDTH + 110     # x의 화면상의 위치 표시
    # y의 화면상의 위치 표시
    y = stair_level * STAIR_HEIGHT + 110
    # y = 6 * STAIR_HEIGHT + 110
    stair_level += 1        #계단의 높이 (최대 12)
    return x, y