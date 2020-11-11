import gfw
from pico2d import *
from background import *
from player import Player
import gobj

canvas_width = 600
canvas_height = 900

def enter():
    gfw.world.init(['bg', 'player'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    bg = FixedBackground('/background.png')
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    global font
    font = gfw.font.load('../res/font' + '/ARCADECLASSIC.TTF', 40)

def update():
    gfw.world.update()

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
