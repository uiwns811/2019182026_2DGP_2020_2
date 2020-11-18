import gfw
from pico2d import *
from background import *
from stairs import Stair
from player import Player
import stairs_gen
import gobj
import time

canvas_width = 700
canvas_height = 1000

def build_world():
    gfw.world.init(['bg', 'stairs', 'player'])
    
    global bg
    bg = FixedBackground('/background.png')
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load('../res/font' + '/ARCADECLASSIC.TTF', 40)

def generate_player():
    global player, bg
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)
  
def generate_stair():    
    global stairs
    for s in range (0, 13):
        stairs = stairs_gen.generate_stair()
    print("generate_stair")
    
    # global stairs, bg
    # for e in range(0, 15):
    #     stairs = Stair()
    # # stairs.bg = bg
    #     gfw.world.add(gfw.layer.stairs, stairs)

    # for stairs in gfw.world.objects_at(gfw.layer.stairs):
    #     gfw.world.add(gfw.layer.stairs, stairs)

def enter():
    center = get_canvas_width() // 2, get_canvas_height() // 2

    build_world()
    generate_player()
    # generate_stair()
    # for e in range (0, 20):

def update():
    #generate_stair()
    gfw.world.update()
    stairs = stairs_gen.generate_stair()
    time.sleep(1)
    sc = gfw.world.count_at(gfw.layer.stairs)
    print('sc : ', sc)
    remove()
    # stairs_gen.update()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()
    font.draw(20, canvas_height - 45, "hello")

def handle_event(e):
    global player, stairs
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE: 
            gfw.pop()
        elif e.key == SDL_KEYDOWN:
            generate_stair()

    if player.handle_event(e):
        return
    #if stair.handle_event(e):
      #  return

def remove():
    if gfw.world.count_at(gfw.layer.stairs) > 20:
        for e in range(0, 20):
            gfw.world.clear_at(gfw.layer.stairs)
        print('================================================')

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()