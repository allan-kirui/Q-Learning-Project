import pygame
from pygame.locals import *

WIDTH = 20
HEIGHT = 20
MARGIN = 2


class App:
    WINDOW_WIDTH = 245
    WINDOW_HEIGHT = 245

    black = (0, 0, 0)
    white = (255, 255, 255)

    green = (0, 255, 0)
    red = (255,0,0)

    grid = []
    size = 11

    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), flags)

        App.running = True
        # looks like the board
        self.grid = []
        for row in range(self.size):
            self.grid.append([])
            for column in range(self.size):
                self.grid[row].append(-100)
        self.grid[0][5] = 100

        aisles = {}  # store locations in a dictionary
        aisles[1] = [i for i in range(1, 10)]
        aisles[2] = [1, 7, 9]
        aisles[3] = [i for i in range(1, 8)]
        aisles[3].append(9)
        aisles[4] = [3, 7]
        aisles[5] = [i for i in range(11)]
        aisles[6] = [5]
        aisles[7] = [i for i in range(1, 10)]
        aisles[8] = [3, 7]
        aisles[9] = [i for i in range(11)]
        for row in range(1, 10):
            for col in aisles[row]:
                self.grid[row][col] = -1

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0]
                    row = pos[1]

            App.screen.fill(self.white)
            for row in range(self.size):
                for col in range(self.size):
                    color = self.white
                    if self.grid[row][col] == 100:
                        color = self.green
                    elif self.grid[row][col] == -100:
                        color = self.black

                    pygame.draw.rect(App.screen,
                                     color,
                                     [(MARGIN + WIDTH) * col + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    App().run()
