from pico2d import *
import play_mode

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def update():
    play_mode.update()


def render():
    play_mode.draw_world()
    image.draw(660, 490)
    update_canvas()
