import pygame
from Agent import Agent
from Contstants import Colors
from Contstants import FieldConstants as fc
from Board.Board import Board
from Button import Button

MARGIN = 5
FIELD_SIZE = 20
LEFT_PANEL_WIDTH = 200
LEFT_PANEL_HEIGHT = 0
FPS = 60
BUTTONS_POS_X = 20
BUTTONS_POS_Y = 20
BUTTONS_SPACING = 50
COLOR_BACKGROUND = Colors.BLACK
COLOR_AGENT = Colors.PINK
FIELDS = fc.FIELDS
INDEX_WALL = fc.INDEX_WALL


WINDOW_NAME = "AI Project ML AK"


class Window:
    grid = None
    board = None
    buttonMove = None
    buttonReset = None
    buttonRandom = None
    agent = None
    windowWidth = None
    windowHeight = None
    scr = None
    path = None

    def initButtons(self, scr, button_x, button_y):
        self.buttonMove = Button(scr,
                                 "Move",
                                 (button_x, button_y),
                                 font=30,
                                 feedback="Move")

        self.buttonRandom = Button(scr,
                                   "Randomize",
                                   (button_x, button_y + BUTTONS_SPACING),
                                   font=30,
                                   feedback="Randomize")

        self.buttonReset = Button(scr,
                                  "Reset",
                                  (button_x, button_y + BUTTONS_SPACING*2),
                                  font=30,
                                  feedback="Reset")

    def showButtons(self):
        self.buttonMove.show()
        self.buttonReset.show()
        self.buttonRandom.show()

    def buttonActions(self, event):
        if self.buttonMove.clickMove(event):
            pos = self.agent.getAgentPosition()
            self.path = self.agent.get_shortest_path(pos[0], pos[1])
        if self.buttonReset.clickMove(event):
            self.path = []
        if self.buttonRandom.clickMove(event):
            self.path = []
            pos = self.board.randomStart()
            self.agent.setAgentPosition(pos[0], pos[1])

    def __init__(self):
        self.grid = []
        self.board = Board()
        self.windowWidth = self.board.getBoardCols() * (FIELD_SIZE + MARGIN) + 5 + LEFT_PANEL_WIDTH
        self.windowHeight = self.board.getBoardRows() * (FIELD_SIZE + MARGIN) + 5 + LEFT_PANEL_HEIGHT
        pygame.init()
        self.scr = pygame.display.set_mode([self.windowWidth, self.windowHeight])
        self.initButtons(self.scr, self.windowWidth - LEFT_PANEL_WIDTH + BUTTONS_POS_X, BUTTONS_POS_Y)
        self.agent = Agent(self.board)
        self.agent.setAgentPosition(3, 9)
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
                    col = pos[0] // (FIELD_SIZE + MARGIN)
                    row = pos[1] // (FIELD_SIZE + MARGIN)
                    if 0 <= row <= self.board.getBoardRows() and 0 <= col <= self.board.getBoardCols():
                        if not self.board.isWall(row, col):
                            self.agent.setAgentPosition(row, col)
                            self.path = []

                self.buttonActions(event)

            self.scr.fill(COLOR_BACKGROUND)

            self.showButtons()

            for row in range(self.board.getBoardRows()):
                for col in range(self.board.getBoardCols()):
                    points = self.board.getFieldPoints(row, col)
                    color = fc.FIELD_QuePasa["Color"]
                    for index in range(len(FIELDS)):
                        if points == FIELDS[index]["Pts"]:
                            color = FIELDS[index]["Color"]

                    field = [row, col]
                    pos = self.agent.getAgentPosition()
                    if pos[0] == row and pos[1] == col:
                        color = COLOR_AGENT
                    if self.path is not None and field in self.path:
                        color = COLOR_AGENT

                    pygame.draw.rect(self.scr,
                                     color,
                                     [(MARGIN + FIELD_SIZE) * col + MARGIN,
                                      (MARGIN + FIELD_SIZE) * row + MARGIN,
                                      FIELD_SIZE,
                                      FIELD_SIZE])

            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()


if __name__ == '__main__':
    window = Window()
    window.run()
