import pygame
from pygame.locals import *


class App:
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 240

    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), flags)

        App.running = True

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
        pygame.quit()


if __name__ == '__main__':
    App().run()
