import gfw
from pico2d import *
from background import *
from stairs import Stair
from player import Player
import gobj

canvas_width = 700
canvas_height = 900

def build_world():
    gfw.world.init(['bg', 'stair', 'player'])
    
    global bg
    bg = FixedBackground('/background.png')
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load('../res/font' + '/ARCADECLASSIC.TTF', 40)

def generate_player():
    global player
    player = Player()
    global bg
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)
  
def generate_stair():
    # global stair
    # stair = Stair(0, 10)    
    # stair.bg = bg
    # gfw.world.add(gfw.layer.stair, stair)
    x, y = Stair.generate_stair()
    fn = 'stairs.png'
    stair = gobj.AnimObject(fn, (x,y), 10)
    gfw.world.add(gfw.layer.stair, stair)

def enter():
    center = get_canvas_width() // 2, get_canvas_height() // 2

    build_world()
    generate_player()
    for e in range (0, 15):
        generate_stair()

def update():
    gfw.world.update()
    #stair_gen.update()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()
    font.draw(20, canvas_height - 45, "hello")

def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE: 
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()