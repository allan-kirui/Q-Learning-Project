import numpy as np

# action representations: 0 = up, 1 = right, 2 = down, 3 = left
actions = ['up', 'right', 'down', 'left']


class Agent:
    TRAINING_SESSIONS_NUMBER = 40000

    pos_row = None
    pos_col = None
    environment_row = None
    environment_col = None
    board = None
    q_values = None
    epsilon = None
    discount_factor = None
    learning_rate = None

    def __init__(self, board):
        self.board = board
        self.environment_row = board.getBoardRows()
        self.environment_col = board.getBoardCols()
        self.q_values = np.zeros((self.environment_row, self.environment_col, 4))
        self.epsilon = 0.9
        self.discount_factor = 0.9
        self.learning_rate = 0.9

    # Chooses a random, non-black field
    def get_starting_field(self):
        current_row = np.random.randint(self.environment_row)
        current_col = np.random.randint(self.environment_col)

        while self.board.isWall(current_row, current_col):
            current_row = np.random.randint(self.environment_row)
            current_col = np.random.randint(self.environment_col)
        return current_row, current_col

    # define an epsilon greedy algorithm that will choose which action to take next
    def get_next_action(self, current_row, current_col, eps):
        # if a randomly chosen value between 0 and 1 is less than epsilon,
        # then choose the most promising value from the Q-table for this state.
        # if current_row < self.environment_col and current_col < self.environment_row:
        rando = np.random.rand()
        if rando < eps:
            max = np.argmax(self.q_values[current_row, current_col])
            return max
        else:  # choose a random action
            return np.random.randint(4)

    def get_next_loc(self, current_row, current_col, action):
        next_row = current_row
        next_col = current_col
        if actions[action] == 'up' and current_row > 0:
            next_row -= 1
        elif actions[action] == 'down' and current_row < self.environment_row - 1:
            next_row += 1
        elif actions[action] == 'left' and current_col > 0:
            next_col -= 1
        elif actions[action] == 'right' and current_col < self.environment_col - 1:
            next_col += 1
        return next_row, next_col

    def setAgentPosition(self, row, col):
        self.pos_row = row
        self.pos_col = col

    def getAgentPosition(self):
        return self.pos_row, self.pos_col

    def get_shortest_path(self, start_row, start_col):
        if self.board.isWall(start_row, start_col):
            return []
        else:
            current_row, current_col = start_row, start_col
            shortest_path = [[current_row, current_col]]
            while not self.board.isWall(current_row, current_col):
                action = self.get_next_action(current_row, current_col, 1)
                current_row, current_col = self.get_next_loc(current_row, current_col, action)
                shortest_path.append([current_row, current_col])
            return shortest_path

    # Training the agent
    def train(self):
        for episode in range(self.TRAINING_SESSIONS_NUMBER):
            current_row, current_col = self.get_starting_field()

            while not self.board.isWall(current_row, current_col):
                action = self.get_next_action(current_row, current_col, self.epsilon)
                old_row, old_col = current_row, current_col
                current_row, current_col = self.get_next_loc(current_row, current_col, action)
                reward = self.board.board[current_row][current_col]
                if reward == -50 or reward == -6:
                    pass
                old_q_val = self.q_values[old_row, old_col, action]
                temporal_difference = reward + (self.discount_factor * np.max(
                    self.q_values[current_row, current_col])) - old_q_val

                # updating the new Q_val for prev state and action
                new_q_val = old_q_val + (self.learning_rate * temporal_difference)
                self.q_values[old_row, old_col, action] = new_q_val

        print("Finished training")
