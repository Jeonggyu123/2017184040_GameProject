import game_framework
import pygame
import Galaga_play_state

running = True
image = None
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def enter():
    global image
    image = pygame.image.load('game_over.png')

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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(image, image.get_rect())
    pygame.display.flip()