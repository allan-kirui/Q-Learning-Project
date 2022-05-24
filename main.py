from Agent import Agent
from Board import Board

if __name__ == '__main__':
    board = Board()
    board.printBoard()

    agent = Agent(board)
    agent.train()
    print(agent.get_shortest_path(3,9))
