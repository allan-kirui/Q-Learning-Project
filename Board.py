import numpy as np

from Field import Field


class Board:
    IKON_WALL = '#'
    IKON_PATH = '.'
    IKON_TARGET = 'Q'
    IKON_QUEPASA = '?'
    IKON_SEPPARATOR = ' '
    PTS_WALL = -100
    PTS_PATH = -1
    PTS_TARGER = 100

    board = None
    row = None
    col = None



    def __init__(self,row,col):
        self.row = row
        self.col = col
        fieldBlack = Field(self.PTS_WALL)
        fieldWhite = Field(self.PTS_PATH)
        fieldGreen = Field(self.PTS_TARGER)
        self.board = [[fieldBlack for i in range(self.row)] for j in range(self.col)]
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

    def print_board_head(self):
    #{
        print("\t ", end="")
        for col in range(self.col):
        #{
            print(col, end=self.IKON_SEPPARATOR)
        #}
        print()
        print("\t ", end="")
        for col in range(self.col):
        #{
            print(" ", end=self.IKON_SEPPARATOR)
        #}
        print()
    #}
    def print_board(self):
        self.print_board_head()
        for row in range(self.row):
        #{
            print(row, end="\t ")
            for col in range(self.col):
            #{
                if self.board[row][col].reward == self.PTS_WALL:
                #{
                    print(self.IKON_WALL, end=self.IKON_SEPPARATOR)
                #}
                elif self.board[row][col].reward == self.PTS_TARGER:
                #{
                    print(self.IKON_TARGET, end=self.IKON_SEPPARATOR)
                #}
                elif self.board[row][col].reward == self.PTS_PATH:
                #{
                    print(self.IKON_PATH, end=self.IKON_SEPPARATOR)
                #}
                else:
                #{
                    print(self.IKON_QUEPASA, end=self.IKON_SEPPARATOR)
                #}
                #print(self.board[row][col].reward,end=" ")
            #}
            print(" ")
        #}




