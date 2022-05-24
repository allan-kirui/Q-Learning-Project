import pygame
import Colors
from Board.Board import Board

MARGIN = 5
FIELD_SIZE = 20
FPS = 60

COLOR_BACKGROUND = Colors.BLACK
COLOR_PATH = Colors.DARK_GREY
COLOR_WALL = Colors.DARK_RED
COLOR_TARGET = Colors.GREEN

WINDOW_NAME = "AI Project ML AK"

class Window:

    grid = None
    board = None
    windowWidth = None
    windowHeight = None

    def __init__(self):
        self.grid = []
        self.board = Board()
        self.windowWidth = self.board.getBoardCols() * (FIELD_SIZE + MARGIN) + 5
        self.windowHeight = self.board.getBoardRows() * (FIELD_SIZE + MARGIN) + 5


    def run(self):
        pygame.init()
        scr = pygame.display.set_mode([self.windowWidth, self.windowHeight])
        pygame.display.set_caption(WINDOW_NAME)
        quit = False
        clock = pygame.time.Clock()
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    break

            scr.fill(COLOR_BACKGROUND)

            for row in range(self.board.getBoardRows()):
                for col in range(self.board.getBoardCols()):
                    color = COLOR_PATH
                    points = self.board.getFieldPoints(row, col)
                    if points< -50:
                        color = COLOR_WALL
                    if points > 50:
                        color = COLOR_TARGET

                    pygame.draw.rect(scr,
                                     color,
                                     [(MARGIN + FIELD_SIZE) * col + MARGIN,
                                      (MARGIN + FIELD_SIZE) * row + MARGIN,
                                      FIELD_SIZE,
                                      FIELD_SIZE])

            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    window = Window()
    window.run()