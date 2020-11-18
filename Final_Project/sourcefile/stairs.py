from pico2d import *
import gfw
import random
import gobj
import time

SPEED_PPS = 3000
MAG_SPEED = 0.15
stair_level = 0
stair_cnt = 0
STAIR_WIDTH = 118
STAIR_HEIGHT = 65

prev_index = random.randint(0, 4)  # 이전 계단의 인덱스
cur_index = 0   # 현재 계단의 인덱스
cnt_dec = 0     # 왼쪽으로의  증가폭
cnt_inc = 0     # 오른쪽으로의 증가폭 

class Stair:
    def __init__(self):
        # super(Stair, self).__init__(fn, (0, 0), 10)
        self.x, self.y = get_canvas_width(), get_canvas_height()
        self.pos = self.x, self.y
        self.image = gfw.image.load(gobj.res('/stairs.png'))
        self.being_born = True
        self.mag = 0
        self.time = get_time()
        self.fps = 10
        self.fcount = 0
        if self.fcount == 0:
            self.fcount = self.image.w // self.image.h
        self.width = self.image.w // self.fcount
        self.height = self.image.h
        self.stair_level = 0
    
    # def update(self):
    
    def generate_stair():
        global stair_level, prev_index, cur_index, cnt_dec, cnt_inc, stair_cnt
        if (stair_level > 12):
            stair_level = 0

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
        stair_cnt += 1
        return (x, y)

    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.fps) % self.fcount
        sx = self.width * fidx
        #elapsed = get_time() - self.time
        #fidx = round(elapsed * self.fps) % self.fcount
        #sx = self.width * fidx
        #size = self.width * self.mag, self.height * self.mag
        self.pos = Stair.generate_stair()
        self.image.clip_draw(sx, 0, self.width, self.height, *self.pos)
        # time.sleep(0.1)

    def update(self):
        if self.y < -STAIR_HEIGHT:
            self.remove()
            print("지워지고있다...")
        
    def handle_event(self, e):
        pair = (e.type, e.key)
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE:
                print("스페이스바 눌림 ㄱㅡ ", self.y)

    def remove(self):
        gfw.world.remove(self)

    # def __del__(self):
    #     print("Removing", self)