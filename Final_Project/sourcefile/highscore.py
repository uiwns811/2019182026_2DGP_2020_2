import pickle
from pico2d import *
import time
import gfw

FILENAME = 'data.pickle'
scores = []
MAX_SCORE_COUNT = 5
last_rank = -1

class Entry:
    def __init__(self, score):
        self.score = score
        self.time = time.time()

def load():
    global font, image
    font = gfw.font.load('../res/font/FlappyFont.TTF', 30)

    global scores
    try:
        f = open(FILENAME, "rb")
        scores = pickle.load(f)
        f.close()
        # print("Scores:", scores)
    except:
        print("No highscore file")

def save():
    f = open(FILENAME, "wb")
    pickle.dump(scores, f)
    f.close()

def add(score):
    global scores, last_rank
    entry = Entry(score)
    inserted = False
    for i in range(len(scores)):
        e = scores[i]
        if e.score < entry.score:
            scores.insert(i, entry)
            inserted = True
            last_rank = i + 1
            break
    if not inserted:
        scores.append(entry)
        last_rank = len(scores)

    if (len(scores) > MAX_SCORE_COUNT):
        scores.pop(-1)
    if last_rank <= MAX_SCORE_COUNT:
        save()

def draw():
    global font, last_rank
    no = 1
    x = get_canvas_width() // 3
    y = get_canvas_height() // 2
    for e in scores:
        str = "{:2d} {:7.1f}".format(no, e.score)
        color = (0, 128, 200) if no == last_rank else (139, 69, 19)
        font.draw(x, y, str, color)
        #font.draw(300, y, time.asctime(time.localtime(e.time)), color)
        y -= 30
        no += 1

def update():
    pass