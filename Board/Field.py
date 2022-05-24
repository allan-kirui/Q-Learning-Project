class Field:
    color = None
    x = None
    y = None
    reward = None

    def __init__(self, reward):
        self.reward = reward

    def setColor(self, color):
        self.color = color

    def setReward(self, reward):
        self.reward = reward


