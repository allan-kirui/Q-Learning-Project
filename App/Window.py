import pygame

from Agent import Agent
import Colors
from Board.Board import Board
from Button import Button

MARGIN = 5
FIELD_SIZE = 20
FPS = 60
BUTTON_X = 300
BUTTON_Y = 200
COLOR_BACKGROUND = Colors.BLACK
COLOR_PATH = Colors.WHITE
COLOR_WALL = Colors.DARK_GREY
COLOR_TARGET = Colors.CYAN

WINDOW_NAME = "AI Project ML AK"


class Window:
    grid = None
    board = None
    button = None
    agent = None
    windowWidth = None
    windowHeight = None
    scr = None

    def __init__(self):
        self.grid = []
        self.board = Board()
        self.windowWidth = 500  # self.board.getBoardCols() * (FIELD_SIZE + MARGIN) + 5
        self.windowHeight = 300  # self.board.getBoardRows() * (FIELD_SIZE + MARGIN) + 5
        pygame.init()
        self.scr = pygame.display.set_mode([self.windowWidth, self.windowHeight])
        self.button = Button(self.scr,
                             "Click here",
                             (BUTTON_X, BUTTON_Y),
                             font=30,
                             bg="navy",
                             feedback="You clicked me")

        self.agent = Agent(self.board)
        self.agent.train()

    def run(self):
        pygame.display.set_caption(WINDOW_NAME)
        quit = False
        clock = pygame.time.Clock()
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (FIELD_SIZE + MARGIN)
                    row = pos[1] // (FIELD_SIZE + MARGIN)
                self.button.click(event)

            self.scr.fill(COLOR_BACKGROUND)
            self.button.show()
            for row in range(self.board.getBoardRows()):
                for col in range(self.board.getBoardCols()):
                    color = COLOR_PATH
                    points = self.board.getFieldPoints(row, col)
                    if points < -50:
                        color = COLOR_WALL
                    if points > 50:
                        color = COLOR_TARGET

                    pygame.draw.rect(self.scr,
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
