from AI.enum.enum import EASY as EASY
from AI.enum.enum import EASY as NORMAL
from AI.enum.enum import EASY as HARD


class DifficultyLevel:
    def __init__(self, name):
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
        else:
            raise ValueError("There is no such option!")
