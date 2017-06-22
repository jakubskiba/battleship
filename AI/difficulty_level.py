from AI.enum.enum import EASY as EASY
from AI.enum.enum import NORMAL as NORMAL
from AI.enum.enum import HARD as HARD


class DifficultyLevel:
    def __init__(self, name=''):
        self.name = name
        self.level = None
        self.set_level(name)

    def set_level(self, name):
        if name == "easy":
            self.level = EASY
        elif name == "normal":
            self.level = NORMAL
        elif name == "hard":
            self.level = HARD
