import game_framework
import pygame
import Galaga_play_state
#from Galaga_play_state import Draw_text

running = True
image = None
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

logo_time = 0.0


def enter():
    global image
    image = pygame.image.load('tuk_credit.png')

def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


def handle_events():

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_framework.quit()

        if event.type == pygame.KEYDOWN and pygame.K_SPACE:
            game_framework.change_state(Galaga_play_state)


def update():
    pass


def draw():
    kill, miss = 1, 10
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(image, image.get_rect())
    # default_font = pygame.font.Font(None, 28)
    # Draw_text(screen, "killed : [] miss : []".format(kill, miss), default_font, 10, 5, (255, 255, 0))
    pygame.display.flip()



# def enter():
#     global image
#     image = load_image('space.png')
#     pass
#
# def exit():
#
#     pass
#
# def update():
#     global logo_time
#     global running
#     if logo_time > 1.0:
#         logo_time = 0
#         running = False
#         game_framework.change_state(Galaga_play_state)      #중단
#     pico2d.time(0.01)
#     logo_time += 0.01
#     open_canvas()
#     pass
#
# def draw():
#     clear_canvas()
#     image.draw(400, 800)
#     update_canvas()
#     pass
#
# def handle_events():
#     events = pico2d.get_events()