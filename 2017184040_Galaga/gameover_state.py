import game_framework
import pygame
import Galaga_play_state
import main_state

running = True
image = None
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
Yellow = (255, 255, 0)

def enter():
    global image
    image = pygame.image.load('game_over.png')

def Draw_text(screen, text, font, x, y, color):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = x, y
    screen.blit(text_obj, text_rect)

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
            game_framework.change_state(main_state)


def update():
    pass


def draw():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(image, image.get_rect())
    default_font = pygame.font.Font(None, 50)
    Draw_text(screen, "GAME OVER", default_font, 400, 200, Yellow)
    pygame.display.flip()
