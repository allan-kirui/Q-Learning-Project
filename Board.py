import numpy as np

from Field import Field


class Board:
    board = None

    def __init__(self):
        fieldBlack = Field(-100)
        fieldWhite = Field(-1)
        fieldGreen = Field(100)
        self.board = [[fieldBlack for i in range(11)] for j in range(11)]
        self.board[0][5] = fieldGreen

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
                self.board[row][col] = fieldWhite

    def print_board(self):
        for row in range(11):
            for col in range(11):
                print(self.board[row][col].reward,end=" ")
            print(" ")


if __name__ == '__main__':
    boards = Board()
    boards.print_board()

