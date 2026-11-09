from pico2d import *
import game_framework
import game_world
import pause_mode
import title_mode
from boy import Boy
from grass import Grass


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        else:
            boy.handle_event(event)



def init():
    global boy


    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

def update():
    game_world.update()


def draw_world():
    clear_canvas()
    game_world.render()


def render():
    draw_world()
    update_canvas()

def finish():
    game_world.clear()


def pause():
    global paused_at
    paused_at = get_time()


def resume():
    boy.idle_started_at += get_time() - paused_at
    keys = SDL_GetKeyboardState(None)
    for key, scancode in ((SDLK_LEFT, SDL_SCANCODE_LEFT), (SDLK_RIGHT, SDL_SCANCODE_RIGHT)):
        if key in boy.pressed_keys and not keys[scancode]:
            event = Event(SDL_KEYUP)
            event.key = key
            boy.handle_event(event)

