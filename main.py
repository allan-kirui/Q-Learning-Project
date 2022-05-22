from Agent import Agent
from Board import Board

if __name__ == '__main__':
    board = Board(11,11)
    board.print_board()

    agent = Agent(board,11,11)
    agent.train()
    print(agent.get_shortest_path(3,9))
