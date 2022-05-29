from random import random
from Contstants import FieldConstants as fc
import numpy as np

from Board import BoardTemplates

IKON_SEPPARATOR = ' '
FIELDS = fc.FIELDS
INDEX_WALL = fc.INDEX_WALL
INDEX_PATH = fc.INDEX_PATH
INDEX_TARGET = fc.INDEX_TARGET
BOARD_TEMPLATE = BoardTemplates.TEMPLATE_2


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
                points = fc.FIELD_QuePasa["Pts"]
                for index in range(len(FIELDS)):
                    if icon == FIELDS[index]["Icon"]:
                        points = FIELDS[index]["Pts"]

                arr.append(points)

            self.board.append(arr)

        return

    def randomStart(self):
        pos_row = np.random.randint(self.rows)
        pos_col = np.random.randint(self.cols)
        while self.board[pos_row][pos_col] == FIELDS[INDEX_WALL]["Pts"]:
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
                icon = fc.FIELD_QuePasa["Icon"]
                for index in range(len(FIELDS)):
                    if points == FIELDS[index]["Pts"]:
                        icon = FIELDS[index]["Icon"]

                print(icon, end=IKON_SEPPARATOR)

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
        # if row < self.cols and col < self.rows:
        # print(row, col)
        if self.board[row][col] == FIELDS[INDEX_WALL]["Pts"] or self.board[row][col] == FIELDS[INDEX_TARGET]["Pts"]:
            return True
        else:
            return False
