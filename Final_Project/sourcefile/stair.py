from pico2d import *
import gfw

MOVE_PPS = 200      # 초당 200픽셀로 움직임
STAIR_WIDTH = 118
STAIR_HEIGHT = 65

class Stair:
    def __init__(self, pos): #생성시 pos, delta를 넘겨줄 것
        self.pos = pos
        self.delta = 1.0
        self.image = gfw.image.load('../res/image/stairs.png')
        self.radius = self.image.w // 2
        self.bb_l = -self.image.w
        self.bb_b = -self.image.h
        self.bb_r = get_canvas_width() + self.image.w
        self.bb_t = get_canvas_height() + self.image.h

    def update(self):
        pass

    def draw(self):
        self.image.draw(*self.pos)

    def out_of_screen(self):    # 내가 화면 밖으로 나갔는지
        x, y = self.pos
        # if self.pos[0] 로 해도 됨
        if x < self.bb_l : return True
        if x > self.bb_r : return True
        if y < self.bb_b : return True
        if y > self.bb_t : return True

        return False

    def down_pos(self):
        x, y = self.pos
        dy = self.delta
        y -= dy * STAIR_HEIGHT
        self.pos = x, y

        if self.out_of_screen():
            gfw.world.remove(self)

    def handle_event(self, e):        
        if e.type == SDL_MOUSEBUTTONDOWN:
            Stair.down_pos(self)