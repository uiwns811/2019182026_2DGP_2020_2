import gfw
from pico2d import *
import background
from player import Player
from stair import *
import stair_gen
from coins import *
import gobj
import time
import random
import collision

canvas_width = 700
canvas_height = 900

def build_world():
    global player
    gfw.world.init(['bg', 'stairs', 'coins', 'player'])

    generate_player()
    generate_stair()
    
    # global bg
    # bg = FixedBackground('/background.png')
    # gfw.world.add(gfw.layer.bg, bg)
    background.init()
    gfw.world.add(gfw.layer.bg, background)

    global font
    font = gfw.font.load('../res/font' + '/ARCADECLASSIC.TTF', 40)

def generate_player():
    global player, bg
    player = Player()
    player.bg = background
    gfw.world.add(gfw.layer.player, player)
    bb = player.get_bb()
    print('player =', bb)
  
def generate_stair():
    print('*****************************hi*************************')    

    # stair_gen.init()    global stairs
    # for s in range (0, 13):
    stairs = stair_gen.update()
    print("generate_stair")

    # global coins
    # sc = random.randint(1, 5)
    # if sc == 3:
    #     coins = Coins((stairs.x, stairs.y), (15, 15))
    #     gfw.world.add(gfw.layer.coins, coins)
    # for s in gfw.world.objects_at(gfw.layer.stairs):
    #     bb = Stair.get_bb(s)
    #     print(bb)

    
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
    # generate_player()
    generate_stair()
    # for e in range (0, 20):

def update():
    #generate_stair()
    gfw.world.update()
    # time.sleep(1)

    remove()
    # stairs_gen.update()

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    font.draw(20, canvas_height - 45, "hello")

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE: 
            gfw.pop()
        elif e.key == SDLK_DOWN:
            generate_stair()
    if e.type == SDL_MOUSEBUTTONDOWN:
        for s in gfw.world.objects_at(gfw.layer.stairs):
            if s.ylevel == 3:
                # Stair.move_pos(s)
                check_stairs(s)
                if check_stairs(s) == True:
                    for s in gfw.world.objects_at(gfw.layer.stairs):
                        Stair.move_pos(s)
            # bb = Stair.get_bb(s)
            # print(bb)
            # sc = gfw.world.count_at(gfw.layer.stairs)
            # print('sc : ', sc)

    # if stairs.handle_event(e):
    #     return

def check_stairs(e):
    if gobj.collides_box(player, e):
        print('Stairs Collision', e)
        return True;
    else:
        return False;

def remove():
    global stairs
    if gfw.world.count_at(gfw.layer.stairs) > 12:
        gfw.world.remove(gfw.layer.stairs)
        gfw.world.empty_trashcan()
        # print('================================================')
        # print(gfw.world.count_at(gfw.layer.stairs))
        # print('================================================')

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()