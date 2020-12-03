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
import highscore

canvas_width = 700
canvas_height = 1000

SCORE_TEXT_COLOR = (255, 0, 0)
STATE_IN_GAME, STATE_GAME_OVER = range(2)

before_setting = 1

def start_game():
    global state
    if state != STATE_GAME_OVER:
        return
    gfw.world.remove(highscore)
    state = STATE_IN_GAME
    global hp
    hp = 100

def build_world():
    global player
    gfw.world.init(['bg', 'stairs', 'coins', 'player', 'ui'])

    generate_player()
    generate_stair()
    
    # global bg
    # bg = FixedBackground('/background.png')
    # gfw.world.add(gfw.layer.bg, bg)
    background.init()
    gfw.world.add(gfw.layer.bg, background)

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

    highscore.load() 

    global game_over_image, font
    game_over_image = gfw.image.load('../res/image/game_over.png')
    font = gfw.font.load('../res/font/FlappyFont.TTF', 35)

    global state, hp
    state = STATE_IN_GAME
    hp = 100

def end_game():
    global state
    state = STATE_GAME_OVER
    highscore.add(hp)
    gfw.world.add(gfw.layer.ui, highscore)

def update():
    global state, hp
    if state != STATE_IN_GAME:
        return


    hp -= gfw.delta_time * 1.2
    gfw.world.update()
    if hp < 0:
        end_game()
    #remove()

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    hp_pos = get_canvas_width() * 2 // 5, get_canvas_height() - 30
    font.draw(*hp_pos, 'HP : %.1f' % hp, SCORE_TEXT_COLOR)

    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height() // 2
        game_over_image.draw(*center)

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE: 
            gfw.pop()
        elif e.key == SDLK_DOWN:
            end_game()
        elif e.key == SDLK_UP:
            start_game()
    if e.type == SDL_MOUSEBUTTONDOWN:
        if player.pos[1] > 400:
            collision_stairs(e)
            global before_setting
        if before_setting < 4:
            for stairobj in gfw.world.objects_at(gfw.layer.stairs):
                print('get_roll : ', player.get_roll())
                stairobj.move_pos_before_4(player.get_roll())
            before_setting += 1
        

    player.handle_event(e)
    # if stairs.handle_event(e):
       #  return

def check_stairs(e):
    if gobj.collides_box(player, e):
        print('Stairs Collision', e)
        return True;
    else:
        return False;

def collision_stairs(e):
    global player
    c_level = 4
    last_stair = 0, 0
    print(player.get_roll())
    for stairobj in gfw.world.objects_at(gfw.layer.stairs):
        if stairobj.get_ylevel() == 13:
            last_stair = stairobj.get_pos()
        stairobj.move_pos(player.get_roll())
    # stair_gen.get_xy(last_stair)
    stair_gen.sub_generate(last_stair)


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