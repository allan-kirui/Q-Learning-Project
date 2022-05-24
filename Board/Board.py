from Board import BoardTemplates

IKON_WALL = '#'
IKON_PATH = '..'
IKON_TARGET = 'Q'
IKON_QUEPASA = '?'
IKON_SEPPARATOR = ' '
PTS_WALL = -100
PTS_PATH = -1
PTS_TARGER = 100
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
        self.printBoard()
        return


    def fillBoard(self):
        self.board = []
        for row in range(self.rows):
            arr = []
            for col in range(self.cols):
                ikon = self.boardTemplate[row][col]
                if ikon == IKON_PATH:
                    arr.append(PTS_PATH)
                elif ikon == IKON_WALL:
                    arr.append(PTS_WALL)
                elif ikon == IKON_TARGET:
                    arr.append(PTS_TARGER)
                else:
                    arr.append(PTS_QUEPASA)

            self.board.append(arr)

        return


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
                    print(IKON_WALL, end=IKON_SEPPARATOR)

                elif points == PTS_TARGER:
                    print(IKON_TARGET, end=IKON_SEPPARATOR)

                elif points == PTS_PATH:
                    print(IKON_PATH, end=IKON_SEPPARATOR)

                else:
                    print(IKON_QUEPASA, end=IKON_SEPPARATOR)

                # print(self.board[row][col].reward,end=" ")

            print(" ")

        return


    def getBoardRows(self):
        return self.rows

    def getBoardCols(self):
        return self.cols

    def getFieldPoints(self, col, row):
        return self.board[col][row]

    def setFieldPoints(self, col, row, points):
        self.board[col][row] = points
        return