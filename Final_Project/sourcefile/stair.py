from pico2d import *
import gfw
import gobj

MOVE_PPS = 200      # 초당 200픽셀로 움직임
STAIR_WIDTH = 132
STAIR_HEIGHT = 72
moveLeft = 0
moveRight = 1
# JSON 사용해보자....에휴 이게 뭐하는 짓거리임

class Stair:
    def __init__(self, pos, ylevel, xdirection): #생성시 pos, delta를 넘겨줄 것
        self.x, self.y = pos
        self.image = gfw.image.load('res/image/stairs.png')
        self.radius = self.image.w // 2
        self.width = self.image.w
        self.height = self.image.h
        self.ylevel = ylevel
        self.xdirection = xdirection
        # self.bb_l = -self.image.w
        # self.bb_b = -self.image.h
        # self.bb_r = get_canvas_width() + self.image.w
        # self.bb_t = get_canvas_height() + self.image.h

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_ylevel(self):
        return self.ylevel

    def get_pos(self):
        return self.x, self.y

    def out_of_screen(self):    # 내가 화면 밖으로 나갔는지
        # if self.pos[0] 로 해도 됨
        if self.y < 0: return True
        return False

    def get_bb(self):
        x, y = self.x, self.y
        return x - self.width//2, y - self.height//2, x + self.width//2, y + self.height//2

    def check_x(self):
        if self.xdirection == 0:
            print("moveLeft")
            return moveLeft
        else:
            print("moveRight")
            return moveRight

    def move_pos(self, movedirection):
        #if movedirection == moveLeft:
       #    self.x -= self.image.w
        #else:
        #    self.x += self.image.w
        # self.y -= self.image.h
        # self.left = self.x - self.image.w // 2
        # self.bottom = self.y - self.image.h // 2
        # self.right = self.left + self.image.w
        # self.top = self.bottom + self.image.h
        # self.ylevel -= 1
        # if self.out_of_screen():
        #     gfw.world.remove(self)
        if movedirection == 0:
            self.x -= self.width
        else:
            self.x += self.width
        self.y -= self.image.h
        self.ylevel -= 1

    def move_pos_before_4(self, movedirection):
        if movedirection == 0:
            self.x -= self.width
        else:
            self.x += self.width

    def remove(self):
        if out_of_screen(self):
            gfw.world.remove(self)
            print('stair remove~')

class Coin(Stair):
    def __init__(self, pos, ylevel):
        self.x, self.y = pos
        self.ylevel = ylevel
        self.image = gfw.image.load(gobj.res('/coins.png'))
        self.width = self.image.w
        self.height = self.image.h
        self.radius = self.image.h // 2
        self.time = get_time()
        self.fps = 8
        self.fcount = self.image.w // self.image.h

    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.fps) % self.fcount
        src_size = self.image.h
        dst_size = self.radius * 2
        self.image.clip_draw(src_size * fidx, 0, src_size, src_size, self.x, self.y, dst_size, dst_size)