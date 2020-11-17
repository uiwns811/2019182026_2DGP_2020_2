import gfw
import random
from gobj import *

SPEED_PPS = 3000
MAG_SPEED = 0.15
stair_level = 0
stair_width = 118
stair_height = 65

prev_index = 4  # 이전 계단의 인덱스
cur_index = 0   # 현재 계단의 인덱스
cnt_dec = 0     # 왼쪽으로의  증가폭
cnt_inc = 0     # 오른쪽으로의 증가폭 

class Stair(AnimObject):
    def __init__(self, value):
        fn = 'stairs.png'
        # super(Stair, self).__init__(fn, (0, 0), 10)
        self.image = gfw.image.load(res(fn))
        self.being_born = True
        self.mag = 0
        self.stair_level = 0

    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.fps) % self.fcount
        sx = self.width * fidx
        size = self.width * self.mag, self.height * self.mag
        self.image.clip_draw(sx, 0, self.width, self.height, *self.pos, *size)
    
    # def update(self):
    
    def generate_stair():
        global stair_level, prev_index, cur_index, cnt_dec, cnt_inc
        stair_level += 1        #계단의 높이 (최대 12)
        randcnt = random.randint(0, 1)      # 계단의 증감폭 랜덤값으로 설정
        # i = random.randint(0, 15)
        # x = i % 4
        # x구현하기 
        if randcnt == 0:
            cur_index = prev_index - 1
            prev_index -= 1

        if randcnt == 1:
            cur_index = prev_index + 1
            prev_index += 1

#         if prev_index > 0 :     # 왼쪽으로 
#             print(randcnt)
#             # if (cnt_dec < randcnt) :
#             print("1, ", cnt_dec, randcnt)
#             cur_index = prev_index - 1
#             prev_index -= 1
#             cnt_dec += 1
#         if prev_index <= 0:      # 오른쪽으로
#             print(randcnt)
# #            if (cnt_inc < randcnt) :
#             print("2, ", cnt_inc, randcnt)
#             cur_index = prev_index + 1
#             prev_index += 1
#             cnt_inc += 1
#         if prev_index == 0:
#             cur_index = prev_index + 1
#             prev_index += 1
#             cnt_inc += 1
        x = (cur_index) * stair_width + 110     # x의 화면상의 위치 표시
        # stair_level < 12:
        y = (12 - stair_level) * stair_height + 110     # y의 화면상의 위치 표시
        # else:
            # y = 0 + 110
        # y = get_canvas_height() - 30 - 30 * stair_level
        return (x, y)    

    def remove(self):
        gfw.world.remove(self)

    def __del__(self):
        print("Removing", self)