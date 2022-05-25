from random import random

import numpy as np

from Board import BoardTemplates

WALL_ICON = '#'
PATH_ICON = '.'
TARGET_ICON = 'Q'
IKON_QUEPASA = '?'
IKON_SEPPARATOR = ' '
PTS_WALL = -100
PTS_PATH = -1
PTS_TARGET = 100
PTS_QUEPASA = 0
BOARD_TEMPLATE = BoardTemplates.TEMPLATE_1

class Board:

    rows = None
    cols = None
    board = None
    boardTemplate = None

    def __init__(self):
        print(":: INITIATING BOARD ::")
        self.rows = len(BOARD_TEMPLATE)
        self.cols = len(BOARD_TEMPLATE[0])
        self.boardTemplate = BOARD_TEMPLATE
        self.fillBoard()
        print(self.board)
        self.printBoard()
        return


    def fillBoard(self):
        self.board = []
        for row in range(self.rows):
            arr = []
            for col in range(self.cols):
                icon = self.boardTemplate[row][col]
                if icon == PATH_ICON:
                    arr.append(PTS_PATH)
                elif icon == WALL_ICON:
                    arr.append(PTS_WALL)
                elif icon == TARGET_ICON:
                    arr.append(PTS_TARGET)
                else:
                    arr.append(PTS_QUEPASA)

            self.board.append(arr)

        return

    def randomStart(self):
        pos_row = np.random.randint(self.rows)
        pos_col = np.random.randint(self.cols)
        while self.boardTemplate[pos_row][pos_col] != PATH_ICON:
            pos_row = np.random.randint(self.rows)
            pos_col = np.random.randint(self.cols)
        return pos_row, pos_col

    def printBoardHead(self):
        print("\t ", end="")
        for col in range(self.cols):
            print(col, end=IKON_SEPPARATOR)

        print()
        print("\t ", end="")
        for col in range(self.cols):
            print(" ", end=IKON_SEPPARATOR)

        print()
        return

    def printBoard(self):
        self.printBoardHead()
        for row in range(self.rows):
            print(row, end="\t ")
            for col in range(self.cols):
                points = self.board[row][col]
                if points == PTS_WALL:
                    print(WALL_ICON, end=IKON_SEPPARATOR)

                elif points == PTS_TARGET:
                    print(TARGET_ICON, end=IKON_SEPPARATOR)

                elif points == PTS_PATH:
                    print(PATH_ICON, end=IKON_SEPPARATOR)

                else:
                    print(IKON_QUEPASA, end=IKON_SEPPARATOR)

                # print(self.board[row][col].reward,end=" ")

            print(" ")

        return

    def getBoardRows(self):
        return self.rows

    def getBoardCols(self):
        return self.cols

    def getFieldPoints(self, row, col):
        return self.board[row][col]

    def setFieldPoints(self, row, col, points):
        self.board[row][col] = points
        return

    def isWall(self, row, col):
        if self.board[row][col] == PTS_PATH:
            return False
        else:
            return True
