from pico2d import *
import game_framework
import pause_mode
import play_mode
import title_mode

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_i:
                game_framework.pop_mode(resume_previous=False)
                return
            if event.key == SDLK_ESCAPE:
                game_framework.pop_mode(resume_previous=False)
                game_framework.change_mode(title_mode)
                return
            if event.key == SDLK_p:
                game_framework.push_mode(pause_mode)
                return
            if event.key in (SDLK_0, SDLK_1, SDLK_2):
                play_mode.boy.selected_item = event.key - SDLK_0
                game_framework.pop_mode(resume_previous=False)
                return
        play_mode.boy.handle_event(event)


def update():
    play_mode.update()


def render():
    play_mode.draw_world()
    image.draw(get_canvas_width() / 2, get_canvas_height() / 2)
    update_canvas()


def pause():
    play_mode.pause()


def resume():
    play_mode.resume()
