import gfw
from pico2d import *
import background
from player import Player
from stair import *
import stair_gen
import gobj
import time
import random
# import collision
import highscore

canvas_width = 700
canvas_height = 1000

HP_TEXT_COLOR = (255, 0, 0)
SCORE_TEXT_COLOR = (255, 212, 0)
STATE_IN_GAME, STATE_GAME_OVER = range(2)

before_setting = 1

def start_game():
    global state, stairs, player
    if state != STATE_GAME_OVER:
        return

    gfw.world.remove(highscore)
    gfw.world.clear_at(gfw.layer.stairs)
    player.reset() 

    state = STATE_IN_GAME
    stairs = stair_gen.update()
    global hp, score
    hp = 30
    score = 0

    music_bg.repeat_play()

def end_game():
    global state, player, font_hp
    state = STATE_GAME_OVER
    #player.dead_player()
    highscore.add(score)
    gfw.world.add(gfw.layer.ui, highscore)
    music_bg.stop()
    gameover_bg.play()
    font_hp.draw(200, 200, 'RESTART -> ENTER', (0, 0, 0))

def build_world():
    global player
    gfw.world.init(['bg', 'stairs', 'item', 'player', 'ui'])

    generate_player()
    stair_gen.update()

    background.init()
    gfw.world.add(gfw.layer.bg, background)

def generate_player():
    global player, bg
    player = Player()
    player.bg = background
    gfw.world.add(gfw.layer.player, player)

def enter():
    center = get_canvas_width() // 2, get_canvas_height() // 2

    build_world()

    highscore.load() 

    global game_over_image, font_hp, font_score
    game_over_image = gfw.image.load('res/image/game_over.png')
    font_hp = gfw.font.load('res/font/FlappyFont.TTF', 40)
    font_score = gfw.font.load('res/font/FlappyFont.TTF', 30)

    global music_bg, step_up_bg, gameover_bg
    music_bg = load_music('res/audio/main_bgm.mp3')
    #step_up_bg = load_music('../res/audio/stair_up.mp3')
    gameover_bg = load_music('res/audio/gameover.MP3') 

    global state, hp, score
    state = STATE_IN_GAME
    hp = 30
    score = 0
    start_game()
    music_bg.repeat_play()

def update():
    global state, hp
    if state != STATE_IN_GAME:
        player.dead_player()
        return

    gfw.world.update()

    if hp < 30:
        hp -= gfw.delta_time * 8.0
    elif hp < 60:
        hp -= gfw.delta_time * 15.0
    else: 
        hp -= gfw.delta_time * 20.0
    gfw.world.update()
    if hp < 0.1:
        end_game()


    #remove()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()
    hp_pos = get_canvas_width() * 2 // 5, get_canvas_height() - 30
    score_pos = get_canvas_width() - 200, get_canvas_height() - 100
    font_hp.draw(*hp_pos, 'HP : %.1f' % hp, HP_TEXT_COLOR)
    font_score.draw(*score_pos, 'SCORE : %.f' % score, SCORE_TEXT_COLOR)

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
        elif e.key == SDLK_e:
            end_game()
        elif e.key == SDLK_RETURN:
            start_game()
    if e.type == SDL_MOUSEBUTTONDOWN:
        #step_up_bg.play()
        global state
        if state == STATE_GAME_OVER:
            return

        #step_up_bg.play()
        global before_setting
        if before_setting < 5:
            for stairobj in gfw.world.objects_at(gfw.layer.stairs):
                stairobj.move_pos_before_4(player.get_roll())
            before_setting += 1

        if player.pos[1] > 470:
            move_gen_stairs(e)

        for stairobj in gfw.world.objects_at(gfw.layer.stairs):
            if player.pos[1] < 200:
                if stairobj.get_ylevel() == 1:
                    check_collision_stairs(stairobj)
            elif player.pos[1] < 270:
                if stairobj.get_ylevel() == 2:
                    check_collision_stairs(stairobj)
            elif player.pos[1] < 350:
                if stairobj.get_ylevel() == 3:
                    check_collision_stairs(stairobj)
                
            else:
                if stairobj.get_ylevel() == 4:
                    check_collision_stairs(stairobj)
                
    if state != STATE_GAME_OVER:
        player.handle_event(e)
   
def check_collision_stairs(e):
    global hp, score, state
    dead_by_stairs()
    if gobj.collides_box(player, e):
        print('Stairs Collision', e)
        hp += 2
        score += 1.0
        return True;
    else:
        
        return False

def move_gen_stairs(e):
    global player
    c_level = 4
    last_stair = 0, 0
    print(player.get_roll())
    for stairobj in gfw.world.objects_at(gfw.layer.stairs):
        if stairobj.get_ylevel() == 13:
            last_stair = stairobj.get_pos()
        stairobj.move_pos(player.get_roll())
    stair_gen.get_xy(last_stair)
    stair_gen.sub_generate(last_stair)

def dead_by_stairs():
    global player, state
    for stairobj in gfw.world.objects_at(gfw.layer.stairs):
        if player.pos[1] < 200:
            if stairobj.get_ylevel() == 1:
                 if abs(stairobj.x - player.pos[0]) > 100:
                    end_game()
        elif player.pos[1] < 270:
            if stairobj.get_ylevel() == 2:
                if abs(stairobj.x - player.pos[0]) > 100:
                    end_game()
        elif player.pos[1] < 350:
            if stairobj.get_ylevel() == 3:
                if abs(stairobj.x - player.pos[0]) > 50:
                    end_game()
        else:
            if stairobj.get_ylevel() == 4:
                if abs(stairobj.x - player.pos[0]) > 50:
                    end_game()


def remove():
    global stairs
    if gfw.world.count_at(gfw.layer.stairs) > 12:
        gfw.world.remove(gfw.layer.stairs)
        gfw.world.empty_trashcan()
def exit():
    global music_bg, wav_step_up, gameover_bg
    del music_bg
    #del wav_step_up
    del gameover_bg

if __name__ == '__main__':
    gfw.run_main()